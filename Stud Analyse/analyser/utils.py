# analyser/utils.py
from analyser.models import StudentMark, Attendance, StudentActivity
import pandas as pd

def ai_analyze_student_performance():
    """
    Analyze student performance based on:
    - Marks (maths, science, english)
    - Attendance
    - Activity participation
    """
    # Get all students from marks table (assuming every student has a mark record)
    students = StudentMark.objects.all()
    data = []

    for student in students:
        # --- Marks %
        total_possible_marks = 300  # 3 subjects * 100
        marks_total = student.maths + student.science + student.english
        marks_percent = (marks_total / total_possible_marks) * 100

        # --- Attendance %
        attendance_records = Attendance.objects.filter(student__rollno=student.enrollment_no)
        if attendance_records.exists():
            total_attended = sum([a.attended_days for a in attendance_records])
            total_days = sum([a.total_days for a in attendance_records])
            attendance_percent = (total_attended / total_days) * 100 if total_days else 0
        else:
            attendance_percent = 0

        # --- Activity %
        activities = StudentActivity.objects.filter(enrollment_number=student.enrollment_no)
        if activities.exists():
            total_activity_score = len(activities) * 10  # each activity scored as 10 points
            activity_percent = min((total_activity_score / 50) * 100, 100)  # normalize to 100%
        else:
            activity_percent = 0

        # --- Overall weighted score ---
        overall_score = (marks_percent * 0.6) + (attendance_percent * 0.3) + (activity_percent * 0.1)

        # --- Classify performance ---
        if overall_score >= 70:
            level = "High"
        elif overall_score >= 40:
            level = "Medium"
        else:
            level = "Low"

        data.append({
            "student_name": student.student_name,
            "enrollment_no": student.enrollment_no,
            "marks_percent": round(marks_percent, 2),
            "attendance_percent": round(attendance_percent, 2),
            "activity_percent": round(activity_percent, 2),
            "overall_score": round(overall_score, 2),
            "performance_level": level
        })

    # Return as list of dicts to render in template
    return data
