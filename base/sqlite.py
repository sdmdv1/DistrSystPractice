import sqlite3

DB_PATH='myDB.db'

def initDB():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            sex TEXT,
            birth_date TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS episodes (
            episode_id TEXT PRIMARY KEY,
            patient_id TEXT NOT NULL REFERENCES patients(patient_id),
            time_stamp TEXT NOT NULL,
            heart_rate_bpm INTEGER,
            blood_pressure_systolic INTEGER,
            blood_pressure_diastolic INTEGER,
            oxygen_saturation INTEGER,
            chest_pain_level INTEGER,
            dyspnea_level INTEGER
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
