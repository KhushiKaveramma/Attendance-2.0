from database import attendance
from datetime import datetime


def mark_attendance(emp_id, name):
    today_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check if attendance already exists today
    existing_record = attendance.find_one({
        "employee_id": emp_id,
        "date": today_date
    })

    if existing_record:
        print(f"Attendance already marked today for {name}")
        return

    # Create new attendance record
    record = {
        "employee_id": emp_id,
        "name": name,
        "date": today_date,
        "time": current_time,
        "status": "Present"
    }

    attendance.insert_one(record)

    print(f"Attendance marked successfully for {name} at {current_time}")