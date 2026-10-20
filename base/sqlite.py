import sqlite3

conn=sqlite3.connect('myDB.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id TEXT NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        sex TEXT,
        birth_date TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS episodes (
        id TEXT NOT NULL,
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
