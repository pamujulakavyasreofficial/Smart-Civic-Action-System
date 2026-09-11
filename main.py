from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Smart Civic Action System",
        "status": "Running"
    }

@app.post("/complaints")
def create_complaint_api(complaint: dict):
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

    return {
        "message": "Complaint created successfully",
        "complaint": complaint
    }

@app.get("/complaints")
def get_complaints():
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    conn.close()

    complaints = []

    for row in rows:
        complaints.append({
            "complaint_id": row[0],
            "waste_count": row[1],
            "severity": row[2],
            "latitude": row[3],
            "longitude": row[4],
            "location": row[5],
            "status": row[6],
            "created_at": row[7]
        })

    return complaints