CREATE TABLE IF NOT EXISTS firearms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    caliber TEXT,
    serial_number TEXT UNIQUE NOT NULL,
    current_owner_id INTEGER,
    photo_side TEXT,   -- path to photo showing side serial number
    photo_bottom TEXT, -- path to photo showing bottom serial number
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT,
    is_active INTEGER DEFAULT 1, -- 1 = active, 0 = inactive
    FOREIGN KEY (current_owner_id) REFERENCES employees(id)
);

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    employee_number TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    site_id INTEGER,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT,
    is_active INTEGER DEFAULT 1, -- 1 = active, 0 = inactive
    FOREIGN KEY (site_id) REFERENCES sites(id)
);

CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    supervisor_phone TEXT,
    manager_phone TEXT,
    assistant_manager_phone TEXT
);

CREATE TABLE IF NOT EXISTS ownership_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firearm_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    date_issued TEXT NOT NULL,
    date_returned TEXT,
    FOREIGN KEY (firearm_id) REFERENCES firearms(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE IF NOT EXISTS armourer_inspections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firearm_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    result TEXT CHECK(result IN ('Pass', 'Fail')),
    pdf_path TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT,
    FOREIGN KEY (firearm_id) REFERENCES firearms(id)
);

CREATE TABLE IF NOT EXISTS function_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firearm_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    result TEXT CHECK(result IN ('Pass', 'Fail')),
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT,
    FOREIGN KEY (firearm_id) REFERENCES firearms(id)
);


--INSERT INTO firearms (make, model, caliber, serial_number)
--VALUES ('Glock', '19', '9mm', 'ABC123');
--
--INSERT INTO employees (first_name, last_name, employee_number, phone_number)
--VALUES ('John', 'Doe', 'EMP001', '555-1234');
--
--INSERT INTO sites (name, address, supervisor_phone, manager_phone, assistant_manager_phone)
--VALUES ('Main Armory', '123 Base St', '555-0001', '555-0002', '555-0003');
--
--INSERT INTO ownership_history (firearm_id, employee_id, date_issued)
--VALUES (1, 1, '2025-05-14');
--
--INSERT INTO armourer_inspections (firearm_id, date, result, pdf_path)
--VALUES (1, '2025-05-14', 'Pass', 'inspections/ABC123_2025-05-14.pdf');
