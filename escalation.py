def check_escalation(severity):
    if severity == "High":
        return "Escalation Required"
    else:
        return "No Escalation"