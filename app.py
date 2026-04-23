from flask import Flask, render_template, request, jsonify
import database
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize DB on startup
database.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database_view')
def database_view():
    total_students = database.get_total_students()
    return render_template('database.html', total_students=total_students)

@app.route('/api/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'}), 400
        
    if file and (file.filename.endswith('.csv') or file.filename.endswith('.txt')):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        try:
            report = database.import_csv(filepath)
            return jsonify({
                'success': True,
                'report': report,
                'message': f"Import complete: {len(report['added'])} added, "
                           f"{len(report['id_conflicts'])} ID conflict(s), "
                           f"{len(report['name_conflicts'])} name duplicate(s)."
            })
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
    else:
        return jsonify({'success': False, 'error': 'Invalid file type. Please upload a CSV.'}), 400

@app.route('/api/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400

    student_id = (data.get('id') or '').strip()
    name       = (data.get('name') or '').strip()
    grade      = (data.get('grade') or '').strip()
    category   = (data.get('category') or '').strip()

    if not all([student_id, name, grade, category]):
        return jsonify({'success': False, 'error': 'All fields (ID, Name, Grade, Category) are required.'}), 400

    result = database.add_student(student_id, name, grade, category)
    if result['success']:
        return jsonify({'success': True, 'message': f'{name} (ID: {student_id}) added successfully.'})
    else:
        return jsonify({'success': False, 'error': result['message'], 'conflict': result.get('conflict')}), 409

@app.route('/api/remove_student', methods=['POST'])
def remove_student():
    data = request.get_json()
    query = str(data.get('query', '')).strip()
    
    if not query:
        return jsonify({'success': False, 'error': 'Search query is required.'}), 400
        
    students = database.find_students(query)
    
    if not students:
        return jsonify({'success': False, 'error': 'Student not found in database.'}), 404
        
    if len(students) > 1:
        return jsonify({
            'success': False, 
            'error': f'Multiple students found matching "{query}". Please use their exact ID to remove them.'
        }), 409
        
    student_id = students[0]['id']
    student_name = students[0]['name']
    
    database.delete_student(student_id)
    
    return jsonify({
        'success': True,
        'message': f'Successfully removed {student_name} (ID: {student_id}).'
    })

@app.route('/api/scan', methods=['POST'])
def scan():
    data = request.get_json()
    if not data or 'student_id' not in data:
        return jsonify({'success': False, 'error': 'No student ID provided'}), 400

    student_id = data['student_id'].strip()
    session    = (data.get('session') or 'lunch').strip().lower()

    if session not in ('breakfast', 'lunch'):
        return jsonify({'success': False, 'error': 'Invalid session. Must be breakfast or lunch.'}), 400

    student = database.get_student_by_id(student_id)
    if not student:
        return jsonify({'success': False, 'error': 'Student not found in database.'}), 404

    # Duplicate check — one scan per student per session per day
    if database.check_duplicate_scan(student_id, session):
        student.pop('category', None)
        return jsonify({
            'success': False,
            'duplicate': True,
            'student': student,
            'error': f"{student['name']} has already been scanned for {session} today."
        }), 409

    try:
        scan_id, scan_time = database.record_scan(student_id, session)
        student.pop('category', None)
        return jsonify({
            'success': True,
            'student': student,
            'scan_time': scan_time.strftime("%I:%M:%S %p"),
            'session': session
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/scans', methods=['GET'])
def get_scans():
    session = request.args.get('session')  # optional: 'breakfast' or 'lunch'
    scans = database.get_recent_scans(session=session)
    from datetime import datetime as dt
    for scan in scans:
        if isinstance(scan['scan_time'], str):
            try:
                parsed = dt.strptime(scan['scan_time'].split('.')[0], "%Y-%m-%d %H:%M:%S")
                scan['scan_time'] = parsed.strftime("%I:%M:%S %p")
            except:
                pass
    return jsonify({'success': True, 'scans': scans})

@app.route('/api/stats', methods=['GET'])
def stats():
    breakfast_scans = database.get_recent_scans(session='breakfast')
    lunch_scans     = database.get_recent_scans(session='lunch')
    return jsonify({
        'success': True,
        'total_scans_today': len(breakfast_scans) + len(lunch_scans),
        'breakfast_count':   len(breakfast_scans),
        'lunch_count':       len(lunch_scans)
    })

@app.route('/api/student_count', methods=['GET'])
def student_count():
    return jsonify({'success': True, 'total': database.get_total_students()})

@app.route('/api/export_scans', methods=['GET'])
def export_scans():
    import io
    import csv
    from flask import Response
    
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    session = request.args.get('session')
    
    if session == 'all':
        session = None
        
    if not start_date or not end_date:
        return "Missing date parameters", 400
        
    scans = database.get_scans_for_export(start_date, end_date, session)
    
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Date', 'Time', 'Session', 'Student ID', 'Name', 'Grade', 'Category'])
    
    for row in scans:
        cw.writerow([
            row.get('scan_date', ''),
            row.get('scan_time', ''),
            row.get('session', '').capitalize(),
            row.get('student_id', ''),
            row.get('name', ''),
            row.get('grade', ''),
            row.get('category', '')
        ])
        
    output = si.getvalue()
    si.close()
    
    filename = f"scans_export_{start_date}_to_{end_date}.csv"
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
