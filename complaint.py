from datetime import datetime

def create_complaint(waste_count, severity, location_data):
    complaint = {
        "complaint_id": "CMP-" + datetime.now().strftime("%Y%m%d%H%M%S"),
        "waste_count": waste_count,
        "severity": severity,
        "latitude": location_data["latitude"],
        "longitude": location_data["longitude"],
        "location": location_data["location"],
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return complaint