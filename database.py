import sqlite3
import csv
import datetime

DB_NAME = 'school_scans.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Create students table
    # ID is TEXT to handle IDs with leading zeros or alphanumeric characters if needed
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    
    # Create scans table (with session column)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            scan_time DATETIME NOT NULL,
            session TEXT NOT NULL DEFAULT 'lunch',
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')

    # Migration: add session column to existing databases that don't have it
    try:
        cursor.execute("ALTER TABLE scans ADD COLUMN session TEXT NOT NULL DEFAULT 'lunch'")
    except Exception:
        pass  # Column already exists

    conn.commit()
    conn.close()

def import_csv(filepath):
    """
    Imports students from a CSV file without overwriting existing records.
    Returns a detailed report dict with:
      - added: list of successfully added students
      - id_conflicts: list of rows skipped because the ID already exists
      - name_conflicts: list of rows skipped because the name already exists
      - invalid_rows: list of rows skipped due to bad formatting
    """
    conn = get_connection()
    cursor = conn.cursor()

    added = []
    id_conflicts = []
    name_conflicts = []
    invalid_rows = []

    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader, start=1):
            if len(row) < 4:
                invalid_rows.append({'row': i, 'data': ','.join(row)})
                continue

            student_id = row[0].strip()
            name = row[1].strip()
            grade = row[2].strip()
            category = row[3].strip()

            if not student_id or not name:
                invalid_rows.append({'row': i, 'data': ','.join(row)})
                continue

            # Check for existing ID
            cursor.execute('SELECT id, name FROM students WHERE id = ?', (student_id,))
            existing_by_id = cursor.fetchone()
            if existing_by_id:
                id_conflicts.append({
                    'row': i,
                    'attempted_id': student_id,
                    'attempted_name': name,
                    'existing_name': existing_by_id['name']
                })
                continue

            # Check for existing name (case-insensitive)
            cursor.execute('SELECT id, name FROM students WHERE LOWER(name) = LOWER(?)', (name,))
            existing_by_name = cursor.fetchone()
            if existing_by_name:
                name_conflicts.append({
                    'row': i,
                    'attempted_id': student_id,
                    'attempted_name': name,
                    'existing_id': existing_by_name['id']
                })
                continue

            # Safe to insert
            cursor.execute('''
                INSERT INTO students (id, name, grade, category)
                VALUES (?, ?, ?, ?)
            ''', (student_id, name, grade, category))
            added.append({'id': student_id, 'name': name, 'grade': grade})

    conn.commit()
    conn.close()

    return {
        'added': added,
        'id_conflicts': id_conflicts,
        'name_conflicts': name_conflicts,
        'invalid_rows': invalid_rows
    }

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return dict(student) if student else None

def add_student(student_id, name, grade, category):
    """
    Adds a single student. Returns a dict:
      {'success': True} on success, or
      {'success': False, 'conflict': 'id'|'name', 'message': str} on conflict.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check ID
    cursor.execute('SELECT name FROM students WHERE id = ?', (student_id,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return {
            'success': False,
            'conflict': 'id',
            'message': f"ID {student_id} is already assigned to \"{existing['name']}\"."
        }

    # Check name (case-insensitive)
    cursor.execute('SELECT id FROM students WHERE LOWER(name) = LOWER(?)', (name,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return {
            'success': False,
            'conflict': 'name',
            'message': f"A student named \"{name}\" already exists with ID {existing['id']}."
        }

    cursor.execute(
        'INSERT INTO students (id, name, grade, category) VALUES (?, ?, ?, ?)',
        (student_id, name, grade, category)
    )
    conn.commit()
    conn.close()
    return {'success': True}

def find_students(query):
    """
    Search for a student by exact ID or name (case-insensitive).
    Returns a list of student dicts.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Try exact ID match first
    cursor.execute('SELECT * FROM students WHERE id = ?', (query,))
    students = cursor.fetchall()
    
    if not students:
        # Try exact name match (case-insensitive)
        cursor.execute('SELECT * FROM students WHERE LOWER(name) = LOWER(?)', (query,))
        students = cursor.fetchall()
        
    conn.close()
    return [dict(s) for s in students]

def delete_student(student_id):
    """
    Deletes a student and all their associated scans from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM scans WHERE student_id = ?', (student_id,))
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    
    conn.commit()
    conn.close()
    return True


def check_duplicate_scan(student_id, session):
    """
    Returns True if the student has already been scanned in
    the given session (breakfast/lunch) on today's date.
    """
    conn = get_connection()
    cursor = conn.cursor()
    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end   = today_start + datetime.timedelta(days=1)
    cursor.execute('''
        SELECT id FROM scans
        WHERE student_id = ?
          AND session    = ?
          AND scan_time >= ?
          AND scan_time <  ?
        LIMIT 1
    ''', (student_id, session, today_start, today_end))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def record_scan(student_id, session='lunch'):
    conn = get_connection()
    cursor = conn.cursor()
    now = datetime.datetime.now()
    cursor.execute('''
        INSERT INTO scans (student_id, scan_time, session)
        VALUES (?, ?, ?)
    ''', (student_id, now, session))
    conn.commit()
    scan_id = cursor.lastrowid
    conn.close()
    return scan_id, now

def get_recent_scans(session=None, limit=200):
    conn = get_connection()
    cursor = conn.cursor()

    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end   = today_start + datetime.timedelta(days=1)

    if session:
        cursor.execute('''
            SELECT scans.id, scans.scan_time, scans.session,
                   students.id as student_id, students.name, students.grade
            FROM scans
            JOIN students ON scans.student_id = students.id
            WHERE scans.session = ?
              AND scans.scan_time >= ?
              AND scans.scan_time <  ?
            ORDER BY scans.scan_time DESC
            LIMIT ?
        ''', (session, today_start, today_end, limit))
    else:
        cursor.execute('''
            SELECT scans.id, scans.scan_time, scans.session,
                   students.id as student_id, students.name, students.grade
            FROM scans
            JOIN students ON scans.student_id = students.id
            WHERE scans.scan_time >= ?
              AND scans.scan_time <  ?
            ORDER BY scans.scan_time DESC
            LIMIT ?
        ''', (today_start, today_end, limit))

    scans = cursor.fetchall()
    conn.close()
    return [dict(row) for row in scans]


def get_total_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM students')
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_total_scans_today():
    conn = get_connection()
    cursor = conn.cursor()
    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    cursor.execute('SELECT COUNT(*) FROM scans WHERE scan_time >= ?', (today_start,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_scans_for_export(start_date_str, end_date_str, session):
    """
    Returns scan records for export filtered by date and session.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        # Include the entire end_date
        end_date = end_date + datetime.timedelta(days=1)
    except ValueError:
        return []

    query = '''
        SELECT DATE(scans.scan_time) as scan_date,
               TIME(scans.scan_time) as scan_time,
               scans.session,
               students.id as student_id,
               students.name,
               students.grade,
               students.category
        FROM scans
        JOIN students ON scans.student_id = students.id
        WHERE scans.scan_time >= ? AND scans.scan_time < ?
    '''
    params = [start_date, end_date]

    if session and session in ('breakfast', 'lunch'):
        query += ' AND scans.session = ?'
        params.append(session)

    query += ' ORDER BY scans.scan_time DESC'

    cursor.execute(query, params)
    scans = cursor.fetchall()
    conn.close()
    return [dict(row) for row in scans]
