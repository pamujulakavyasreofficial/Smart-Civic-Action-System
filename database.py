import sqlite3

def save_complaint(complaint):
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            complaint_id TEXT PRIMARY KEY,
            waste_count INTEGER,
            severity TEXT,
            latitude REAL,
            longitude REAL,
            location TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        INSERT OR REPLACE INTO complaints
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        complaint["complaint_id"],
        complaint["waste_count"],
        complaint["severity"],
        complaint["latitude"],
        complaint["longitude"],
        complaint["location"],
        complaint["status"],
        complaint["created_at"]
    ))

    conn.commit()
    conn.close()