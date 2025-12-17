cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cyber_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_type TEXT,
    description TEXT,
    reported_on DATE
)
''')

conn.commit()
