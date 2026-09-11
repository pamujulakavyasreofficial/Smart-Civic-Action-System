from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import sqlite3
import os

from severity import calculate_severity
from location import get_location
from complaint import create_complaint
from escalation import check_escalation
from tracking import update_status
from database import save_complaint
from data_analysis import get_report


# --------------------------------------------------
# FASTAPI APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="Smart Civic Action System",
    description="AI-based Urban Waste Detection and Complaint Management System",
    version="1.0"
)


# --------------------------------------------------
# COMPLAINT DATA MODEL
# --------------------------------------------------

class Complaint(BaseModel):
    complaint_id: str
    waste_count: int
    severity: str
    latitude: float
    longitude: float
    location: str
    status: str
    created_at: str


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# YOLO MODEL
# --------------------------------------------------

model = YOLO("models/best.pt")

os.makedirs("evidence", exist_ok=True)
os.makedirs("uploads", exist_ok=True)


# --------------------------------------------------
# HOME API
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Smart Civic Action System API is running"
    }


# --------------------------------------------------
# CREATE COMPLAINT API
# --------------------------------------------------

@app.post("/complaints")
def create_complaint_api(complaint: Complaint):

    save_complaint(
        complaint.model_dump()
    )

    return {
        "message": "Complaint saved successfully",
        "complaint": complaint.model_dump()
    }


# --------------------------------------------------
# WASTE DETECTION API
# --------------------------------------------------

@app.post("/detect")
async def detect_waste(
    file: UploadFile = File(...)
):

    # --------------------------------------------------
    # CHECK IMAGE
    # --------------------------------------------------

    if not file.content_type:

        return {
            "success": False,
            "message": "No file type received."
        }

    if not file.content_type.startswith("image/"):

        return {
            "success": False,
            "message": "Please upload a valid image file."
        }


    # --------------------------------------------------
    # SAVE UPLOADED IMAGE
    # --------------------------------------------------

    file_name = file.filename

    file_path = os.path.join(
        "uploads",
        file_name
    )


    file_data = await file.read()


    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(file_data)


    # --------------------------------------------------
    # RUN YOLO DETECTION
    # --------------------------------------------------

    results = model(
        file_path
    )


    complaints = []


    # --------------------------------------------------
    # PROCESS YOLO RESULTS
    # --------------------------------------------------

    for result in results:


        # Save detected image
        result.save(
            filename="evidence/detected.jpg"
        )


        # Count detected waste
        waste_count = len(
            result.boxes
        )


        # Calculate severity
        severity = calculate_severity(
            waste_count
        )


        # Get location
        location_data = get_location()


        # Create complaint
        complaint = create_complaint(
            waste_count,
            severity,
            location_data
        )


        # Check escalation
        escalation_status = check_escalation(
            severity
        )


        # Set complaint status
        complaint = update_status(
            complaint,
            "In Progress"
        )


        # Save complaint
        save_complaint(
            complaint
        )


        # --------------------------------------------------
        # GET DETECTED OBJECTS
        # --------------------------------------------------

        objects = []


        for box in result.boxes:


            confidence = float(
                box.conf[0]
            )


            class_id = int(
                box.cls[0]
            )


            class_name = result.names[
                class_id
            ]


            objects.append({

                "object":
                    class_name,

                "confidence":
                    round(
                        confidence,
                        2
                    )

            })


        # --------------------------------------------------
        # CREATE RESPONSE
        # --------------------------------------------------

        complaints.append({

            "complaint_id":
                complaint["complaint_id"],

            "waste_count":
                waste_count,

            "severity":
                severity,

            "latitude":
                location_data["latitude"],

            "longitude":
                location_data["longitude"],

            "location":
                location_data["location"],

            "status":
                complaint["status"],

            "created_at":
                complaint["created_at"],

            "escalation":
                escalation_status,

            "objects":
                objects

        })


    # --------------------------------------------------
    # RETURN RESULT
    # --------------------------------------------------

    return {

        "success":
            True,

        "message":
            "Waste detection completed",

        "filename":
            file_name,

        "results":
            complaints

    }


# --------------------------------------------------
# GET ALL COMPLAINTS
# --------------------------------------------------

@app.get("/complaints")
def get_complaints():

    conn = sqlite3.connect(
        "complaints.db"
    )

    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            complaint_id,
            waste_count,
            severity,
            latitude,
            longitude,
            location,
            status,
            created_at
        FROM complaints
        ORDER BY created_at DESC
    """)


    rows = cursor.fetchall()


    conn.close()


    complaints = []


    for row in rows:

        complaints.append({

            "complaint_id":
                row[0],

            "waste_count":
                row[1],

            "severity":
                row[2],

            "latitude":
                row[3],

            "longitude":
                row[4],

            "location":
                row[5],

            "status":
                row[6],

            "created_at":
                row[7]

        })


    return {

        "total":
            len(complaints),

        "complaints":
            complaints

    }


# --------------------------------------------------
# UPDATE COMPLAINT STATUS
# --------------------------------------------------

@app.put("/complaints/{complaint_id}")
def update_complaint_status(
    complaint_id: str,
    status: str
):

    conn = sqlite3.connect(
        "complaints.db"
    )

    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE complaints
        SET status = ?
        WHERE complaint_id = ?
        """,

        (
            status,
            complaint_id
        )
    )


    conn.commit()


    updated = cursor.rowcount


    conn.close()


    if updated == 0:

        return {

            "success":
                False,

            "message":
                "Complaint not found"

        }


    return {

        "success":
            True,

        "message":
            "Complaint status updated",

        "complaint_id":
            complaint_id,

        "status":
            status

    }


# --------------------------------------------------
# DATA ANALYSIS API
# --------------------------------------------------

@app.get("/analysis")
def analysis():

    report = get_report()


    total = len(
        report
    )


    high = len(
        report[
            report["severity"] == "High"
        ]
    )


    medium = len(
        report[
            report["severity"] == "Medium"
        ]
    )


    low = len(
        report[
            report["severity"] == "Low"
        ]
    )


    pending = len(
        report[
            report["status"] == "Pending"
        ]
    )


    in_progress = len(
        report[
            report["status"] == "In Progress"
        ]
    )


    resolved = len(
        report[
            report["status"] == "Resolved"
        ]
    )


    return {

        "total_complaints":
            total,

        "high_severity":
            high,

        "medium_severity":
            medium,

        "low_severity":
            low,

        "pending":
            pending,

        "in_progress":
            in_progress,

        "resolved":
            resolved

    }