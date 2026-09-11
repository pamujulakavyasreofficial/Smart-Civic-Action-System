def calculate_severity(waste_count):
    if waste_count >= 8:
        return "High"
    elif waste_count >= 4:
        return "Medium"
    else:
        return "Low"