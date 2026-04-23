const translations = {
    en: {
        scanner: "Scanner",
        database: "Database",
        scanner_title: "Student Scanner",
        scanner_subtitle: "Select a session, then scan or enter an ID",
        breakfast: "🌅 Breakfast",
        lunch: "🍽 Lunch",
        breakfast_name: "Breakfast",
        lunch_name: "Lunch",
        scan_input_placeholder: "Scan or type ID here...",
        scan_button: "Scan / Enter",
        breakfast_panel_title: "🌅 Breakfast — Today's Check-ins",
        lunch_panel_title: "🍽 Lunch — Today's Check-ins",
        time_col: "Time",
        id_col: "ID",
        name_col: "Name",
        grade_col: "Grade",
        empty_breakfast: "No students scanned for breakfast yet.",
        empty_lunch: "No students scanned for lunch yet.",
        db_management: "Database Management",
        manage_db: "Manage the student database",
        total_registered: "Total Registered Students",
        export_data: "Export Data",
        export_desc: "Download scan records as a CSV file for Excel analysis.",
        today_breakfast: "🌅 Today's Breakfast",
        today_lunch: "🍽 Today's Lunch",
        advanced_export: "Advanced Export",
        start_date: "Start Date",
        end_date: "End Date",
        session: "Session",
        all_sessions: "All Sessions",
        export_button: "Export to CSV",
        add_manual: "Add a Student Manually",
        manual_desc: "Use this to add a single student without a file. All fields are required.",
        manual_id_placeholder: "e.g. 1042",
        manual_name_placeholder: "e.g. María Torres",
        manual_cat_placeholder: "e.g. A",
        full_name: "Full Name",
        category: "Category",
        add_student_button: "Add Student",
        import_batch: "Import Students (Batch Add)",
        import_desc: "Upload a CSV or TXT file in the format: ID, Name, Grade, Category",
        import_note: "Existing students will not be overwritten. Conflicts are reported below.",
        upload_button: "Upload & Add Students",
        select_grade: "Select Grade",
        pk: "Pre-K",
        k: "Kindergarten (K)",
        g1: "1st Grade", g2: "2nd Grade", g3: "3rd Grade", g4: "4th Grade", g5: "5th Grade",
        g6: "6th Grade", g7: "7th Grade", g8: "8th Grade", g9: "9th Grade", g10: "10th Grade",
        g11: "11th Grade", g12: "12th Grade",
        checked_in_at: "Checked in at",
        already_scanned: "Already Checked In",
        scanned_for_today: "already scanned for {session} today.",
        student_not_found: "Student not found",
        scan_failed: "Scan Failed",
        could_not_connect: "Could not connect to server.",
        select_file: "Please select a file first.",
        uploading: "Uploading...",
        report_added: "✓ Added Successfully",
        report_skipped: "ℹ Already in Database",
        report_failed: "✖ ID Already Claimed",
        report_failed_desc: "These students could not be added because their ID is already used by someone else.",
        report_invalid: "⚠ Invalid / Skipped Rows",
        report_invalid_desc: "These rows had insufficient data and were skipped.",
        row_col: "Row #",
        data_col: "Data",
        current_student: "Current Student",
        new_student: "New Student Attempt",
        remove_student: "Remove a Student",
        remove_desc: "Remove a student and all their scan history from the database.",
        remove_label: "Student ID or Exact Name",
        remove_placeholder: "e.g. 1042 or María Torres",
        remove_button: "Remove Student",
        removing: "Removing..."
    },
    es: {
        scanner: "Escáner",
        database: "Base de Datos",
        scanner_title: "Escáner de Estudiantes",
        scanner_subtitle: "Seleccione una sesión, luego escanee o ingrese un ID",
        breakfast: "🌅 Desayuno",
        lunch: "🍽 Almuerzo",
        breakfast_name: "Desayuno",
        lunch_name: "Almuerzo",
        scan_input_placeholder: "Escanee o escriba el ID aquí...",
        scan_button: "Escanear / Ingresar",
        breakfast_panel_title: "🌅 Desayuno — Registros de Hoy",
        lunch_panel_title: "🍽 Almuerzo — Registros de Hoy",
        time_col: "Hora",
        id_col: "ID",
        name_col: "Nombre",
        grade_col: "Grado",
        empty_breakfast: "Aún no hay estudiantes escaneados para el desayuno.",
        empty_lunch: "Aún no hay estudiantes escaneados para el almuerzo.",
        db_management: "Gestión de Base de Datos",
        manage_db: "Gestionar la base de datos de estudiantes",
        total_registered: "Total de Estudiantes Registrados",
        export_data: "Exportar Datos",
        export_desc: "Descargue los registros de escaneo como un archivo CSV para análisis en Excel.",
        today_breakfast: "🌅 Desayuno de Hoy",
        today_lunch: "🍽 Almuerzo de Hoy",
        advanced_export: "Exportación Avanzada",
        start_date: "Fecha de Inicio",
        end_date: "Fecha de Fin",
        session: "Sesión",
        all_sessions: "Todas las Sesiones",
        export_button: "Exportar a CSV",
        add_manual: "Agregar Estudiante Manualmente",
        manual_desc: "Use esto para agregar un solo estudiante sin un archivo. Todos los campos son obligatorios.",
        manual_id_placeholder: "ej. 1042",
        manual_name_placeholder: "ej. María Torres",
        manual_cat_placeholder: "ej. A",
        full_name: "Nombre Completo",
        category: "Categoría",
        add_student_button: "Agregar Estudiante",
        import_batch: "Importar Estudiantes (Lote)",
        import_desc: "Suba un archivo CSV o TXT en el formato: ID, Nombre, Grado, Categoría",
        import_note: "Los estudiantes existentes no serán sobrescritos. Los conflictos se informan abajo.",
        upload_button: "Subir y Agregar Estudiantes",
        select_grade: "Seleccionar Grado",
        pk: "Pre-K",
        k: "Kindergarten (K)",
        g1: "1er Grado", g2: "2do Grado", g3: "3er Grado", g4: "4to Grado", g5: "5to Grado",
        g6: "6to Grado", g7: "7mo Grado", g8: "8vo Grado", g9: "9no Grado", g10: "10mo Grado",
        g11: "11vo Grado", g12: "12vo Grado",
        checked_in_at: "Registrado a las",
        already_scanned: "Ya Registrado",
        scanned_for_today: "ya fue escaneado para {session} hoy.",
        student_not_found: "Estudiante no encontrado",
        scan_failed: "Error de Escaneo",
        remove_student: "Eliminar un Estudiante",
        remove_desc: "Elimine un estudiante y todo su historial de escaneos de la base de datos.",
        remove_label: "ID del Estudiante o Nombre Exacto",
        remove_placeholder: "ej. 1042 o María Torres",
        remove_button: "Eliminar Estudiante",
        removing: "Eliminando..."
    }
};

let currentLang = localStorage.getItem('preferredLanguage') || 'en';

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('preferredLanguage', lang);
    document.documentElement.lang = lang;

    // Update all elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
            // Preserve child elements if any (like icons or count spans)
            const countSpan = el.querySelector('.tab-count');
            el.textContent = translations[lang][key];
            if (countSpan) el.appendChild(countSpan);
        }
    });

    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[lang][key]) {
            el.placeholder = translations[lang][key];
        }
    });

    // Toggle active flag
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('lang-btn--active', btn.dataset.lang === lang);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    // Language setup
    setLanguage(currentLang);
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
    });

    if (document.querySelector('.scanner-container')) {
        initScannerPage();
    } else if (document.querySelector('.database-container')) {
        initDatabasePage();
    }
});

function initScannerPage() {
    const scanForm      = document.getElementById('scan-form');
    const scannerInput  = document.getElementById('scanner-input');
    const feedbackBanner  = document.getElementById('feedback-banner');
    const feedbackMessage = document.getElementById('feedback-message');
    const feedbackDetails = document.getElementById('feedback-details');

    // --- Tab / Panel state ---
    let activeSession = 'lunch'; // default active tab

    const tabs = document.querySelectorAll('.session-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            activeSession = tab.dataset.session;
            // Update tab active states
            tabs.forEach(t => {
                t.classList.remove('session-tab--active');
                t.setAttribute('aria-selected', 'false');
            });
            tab.classList.add('session-tab--active');
            tab.setAttribute('aria-selected', 'true');
            // Show corresponding panel
            document.querySelectorAll('.session-panel').forEach(p => p.classList.add('hidden'));
            document.getElementById(`panel-${activeSession}`).classList.remove('hidden');
            // Refocus scanner input
            scannerInput.focus();
        });
    });

    // Keep scanner input focused when clicking non-interactive areas
    document.addEventListener('click', (e) => {
        if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'BUTTON' && e.target.tagName !== 'A') {
            scannerInput.focus();
        }
    });

    // Load both lists and counts on page load
    loadSessionList('breakfast');
    loadSessionList('lunch');
    updateTabCounts();

    // --- Scan form submit ---
    scanForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const studentId = scannerInput.value.trim();
        if (!studentId) return;

        scannerInput.value = '';
        scannerInput.focus();

        try {
            const response = await fetch('/api/scan', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ student_id: studentId, session: activeSession })
            });

            const data = await response.json();

            if (data.success) {
                const checkedInAt = translations[currentLang].checked_in_at || "Checked in at";
                showFeedback(
                    'success',
                    `${data.student.name}`,
                    `${checkedInAt} ${data.scan_time} · Grade ${data.student.grade}`
                );
                loadSessionList(activeSession); // refresh active panel
                updateTabCounts();
            } else if (data.duplicate) {
                const alreadyScanned = translations[currentLang].already_scanned || "Already Checked In";
                const sessionName = translations[currentLang][`${activeSession}_name`] || activeSession;
                const scannedForToday = translations[currentLang].scanned_for_today.replace('{session}', sessionName);
                showFeedback(
                    'warning',
                    alreadyScanned,
                    `${data.student.name} ${scannedForToday}`
                );
            } else {
                const scanFailed = translations[currentLang].scan_failed || "Scan Failed";
                const studentNotFound = translations[currentLang].student_not_found || "Student not found";
                showFeedback('error', scanFailed, data.error || studentNotFound);
            }
        } catch (err) {
            showFeedback('error', 'Error', 'Could not connect to server');
            console.error('Scan error:', err);
        }
    });

    // --- Helpers ---

    function showFeedback(type, mainText, subText) {
        feedbackBanner.className = 'feedback-banner';
        feedbackBanner.classList.add(
            type === 'success' ? 'success-banner' :
            type === 'warning' ? 'warning-banner' :
                                 'error-banner'
        );
        feedbackMessage.textContent = mainText;
        feedbackDetails.textContent = subText;
        feedbackBanner.classList.remove('hidden');
        clearTimeout(window.feedbackTimeout);
        window.feedbackTimeout = setTimeout(() => {
            feedbackBanner.classList.add('hidden');
        }, 5000);
    }

    async function loadSessionList(session) {
        try {
            const res = await fetch(`/api/scans?session=${session}`);
            const data = await res.json();
            if (!data.success) return;

            const tbody   = document.getElementById(`tbody-${session}`);
            const emptyEl = document.getElementById(`empty-${session}`);
            tbody.innerHTML = '';

            if (data.scans.length === 0) {
                emptyEl.classList.remove('hidden');
            } else {
                emptyEl.classList.add('hidden');
                data.scans.forEach(scan => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${scan.scan_time}</td>
                        <td>${scan.student_id}</td>
                        <td><strong>${scan.name}</strong></td>
                        <td>${scan.grade}</td>
                    `;
                    tbody.appendChild(tr);
                });
            }
        } catch (err) {
            console.error(`Error loading ${session} list:`, err);
        }
    }

    async function updateTabCounts() {
        try {
            const res = await fetch('/api/stats');
            const data = await res.json();
            if (data.success) {
                document.getElementById('count-breakfast').textContent = data.breakfast_count ?? 0;
                document.getElementById('count-lunch').textContent     = data.lunch_count     ?? 0;
            }
        } catch (err) {
            console.error('Error fetching stats:', err);
        }
    }
}

function initDatabasePage() {
    const uploadForm = document.getElementById('upload-form');
    const csvFile = document.getElementById('csv-file');
    const feedbackText = document.getElementById('upload-feedback');
    const uploadBtn = document.getElementById('upload-btn');

    // --- CSV Export ---
    const exportForm = document.getElementById('export-form');
    if (exportForm) {
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('export-start').value = today;
        document.getElementById('export-end').value = today;

        // --- Quick Exports ---
        const quickBreakfast = document.getElementById('quick-export-breakfast');
        if (quickBreakfast) {
            quickBreakfast.addEventListener('click', () => {
                const params = new URLSearchParams({ start_date: today, end_date: today, session: 'breakfast' });
                window.location.href = `/api/export_scans?${params.toString()}`;
            });
        }
        
        const quickLunch = document.getElementById('quick-export-lunch');
        if (quickLunch) {
            quickLunch.addEventListener('click', () => {
                const params = new URLSearchParams({ start_date: today, end_date: today, session: 'lunch' });
                window.location.href = `/api/export_scans?${params.toString()}`;
            });
        }

        exportForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const start = document.getElementById('export-start').value;
            const end = document.getElementById('export-end').value;
            const session = document.getElementById('export-session').value;
            
            const params = new URLSearchParams({
                start_date: start,
                end_date: end,
                session: session
            });
            
            window.location.href = `/api/export_scans?${params.toString()}`;
        });
    }

    // --- Manual add student ---
    const manualForm = document.getElementById('manual-add-form');
    const manualFeedback = document.getElementById('manual-add-feedback');
    const manualBtn = document.getElementById('manual-add-btn');
    const statNumber = document.querySelector('.stat-number');

    manualForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const id       = document.getElementById('manual-id').value.trim();
        const name     = document.getElementById('manual-name').value.trim();
        const grade    = document.getElementById('manual-grade').value.trim();
        const category = document.getElementById('manual-category').value.trim();

        manualBtn.disabled = true;
        manualBtn.textContent = translations[currentLang].adding || 'Adding...';

        try {
            const res = await fetch('/api/add_student', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id, name, grade, category })
            });
            const data = await res.json();

            if (data.success) {
                showManualFeedback(true, data.message);
                manualForm.reset();
                // Update student count live
                refreshStudentCount();
            } else {
                showManualFeedback(false, data.error);
            }
        } catch (err) {
            const errorMsg = translations[currentLang].could_not_connect || 'Could not connect to server.';
            showManualFeedback(false, errorMsg);
        } finally {
            manualBtn.disabled = false;
            manualBtn.textContent = translations[currentLang].add_student_button;
        }
    });

    function showManualFeedback(isSuccess, message) {
        manualFeedback.textContent = message;
        manualFeedback.className = 'feedback-text ' + (isSuccess ? 'success' : 'error');
        manualFeedback.classList.remove('hidden');
    }

    async function refreshStudentCount() {
        try {
            const res = await fetch('/api/student_count');
            const data = await res.json();
            if (data.success && statNumber) statNumber.textContent = data.total;
        } catch (_) {}
    }

    // --- Remove a student ---
    const removeForm = document.getElementById('remove-student-form');
    const removeFeedback = document.getElementById('remove-feedback');
    const removeBtn = document.getElementById('remove-student-btn');

    if (removeForm) {
        removeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const query = document.getElementById('remove-query').value.trim();

            removeBtn.disabled = true;
            removeBtn.textContent = translations[currentLang].removing || 'Removing...';

            try {
                const res = await fetch('/api/remove_student', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query })
                });
                const data = await res.json();

                if (data.success) {
                    showRemoveFeedback(true, data.message);
                    removeForm.reset();
                    refreshStudentCount();
                } else {
                    showRemoveFeedback(false, data.error);
                }
            } catch (err) {
                const errorMsg = translations[currentLang].could_not_connect || 'Could not connect to server.';
                showRemoveFeedback(false, errorMsg);
            } finally {
                removeBtn.disabled = false;
                removeBtn.textContent = translations[currentLang].remove_button;
            }
        });
    }

    function showRemoveFeedback(isSuccess, message) {
        removeFeedback.textContent = message;
        removeFeedback.className = 'feedback-text ' + (isSuccess ? 'success' : 'error');
        removeFeedback.classList.remove('hidden');
    }

    // --- Batch CSV upload ---
    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const file = csvFile.files[0];
        if (!file) {
            const selectFile = translations[currentLang].select_file || "Please select a file first.";
            showUploadFeedback(false, selectFile);
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        uploadBtn.disabled = true;
        uploadBtn.textContent = translations[currentLang].uploading || "Uploading...";

        try {
            const response = await fetch('/api/upload_csv', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.success) {
                showUploadFeedback(true, data.message);
                csvFile.value = '';
                renderImportReport(data.report);
                refreshStudentCount();
            } else {
                showUploadFeedback(false, data.error || "Upload failed.");
                hideImportReport();
            }
        } catch (error) {
            const errorMsg = translations[currentLang].could_not_connect || "Could not connect to server.";
            showUploadFeedback(false, errorMsg);
            hideImportReport();
            console.error("Upload error:", error);
        } finally {
            uploadBtn.disabled = false;
            uploadBtn.textContent = translations[currentLang].upload_button;
        }
    });


    function showUploadFeedback(isSuccess, message) {
        feedbackText.textContent = message;
        feedbackText.className = 'feedback-text ' + (isSuccess ? 'success' : 'error');
        feedbackText.classList.remove('hidden');
    }

    function hideImportReport() {
        document.getElementById('import-report').classList.add('hidden');
    }

    function renderImportReport(report) {
        const importReport = document.getElementById('import-report');
        importReport.classList.remove('hidden');

        // --- Added ---
        const addedSection = document.getElementById('report-added');
        const addedBody = document.getElementById('report-added-body');
        addedBody.innerHTML = '';
        if (report.added && report.added.length > 0) {
            addedSection.classList.remove('hidden');
            report.added.forEach(s => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${s.id}</td><td><strong>${s.name}</strong></td><td>${s.grade}</td>`;
                addedBody.appendChild(tr);
            });
        } else {
            addedSection.classList.add('hidden');
        }

        // --- ID Conflicts ---
        const idSection = document.getElementById('report-id-conflicts');
        const idBody = document.getElementById('report-id-body');
        idBody.innerHTML = '';
        if (report.id_conflicts && report.id_conflicts.length > 0) {
            idSection.classList.remove('hidden');
            report.id_conflicts.forEach(c => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${c.row}</td><td>${c.attempted_id}</td><td>${c.attempted_name}</td><td>${c.existing_name} (already holds this ID)</td>`;
                idBody.appendChild(tr);
            });
        } else {
            idSection.classList.add('hidden');
        }

        // --- Name Conflicts ---
        const nameSection = document.getElementById('report-name-conflicts');
        const nameBody = document.getElementById('report-name-body');
        nameBody.innerHTML = '';
        if (report.name_conflicts && report.name_conflicts.length > 0) {
            nameSection.classList.remove('hidden');
            report.name_conflicts.forEach(c => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${c.row}</td><td>${c.attempted_id}</td><td>${c.attempted_name}</td><td>${c.existing_id}</td>`;
                nameBody.appendChild(tr);
            });
        } else {
            nameSection.classList.add('hidden');
        }

        // --- Invalid Rows ---
        const invalidSection = document.getElementById('report-invalid');
        const invalidBody = document.getElementById('report-invalid-body');
        invalidBody.innerHTML = '';
        if (report.invalid_rows && report.invalid_rows.length > 0) {
            invalidSection.classList.remove('hidden');
            report.invalid_rows.forEach(r => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${r.row}</td><td><code>${r.data || '(empty)'}</code></td>`;
                invalidBody.appendChild(tr);
            });
        } else {
            invalidSection.classList.add('hidden');
        }
    }
}
