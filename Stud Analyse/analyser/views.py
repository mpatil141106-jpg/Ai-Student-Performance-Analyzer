from django.shortcuts import render,redirect,get_object_or_404
from analyser.models import User,Student,Signup,Attendance,StudentMark,StudentActivity
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import date

def login_page(request):
    return render(request, 'login.html')
# Create your views here.
from django.contrib.auth.hashers import check_password

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .models import User

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")
        role = request.POST.get("role")

        # 🔍 STEP 1: User exist karta hai ya nahi
        user_exist = Signup.objects.filter(
            name__iexact=username
        ).first()

        if not user_exist:
            return render(request, "login.html", {
                "error": "Account does not exist. Please signup first."
            })

        # 🔍 STEP 2: Password + Role verify
        user = Signup.objects.filter(
            name__iexact=username,
            password=password,
        ).first()

        if not user:
            return render(request, "login.html", {
                "error": "Invalid password or role"
            })

        # ✅ LOGIN SUCCESS
        request.session["student_name"] = user.name
        request.session["enrollment_no"] = user.senroll
        request.session["role"] = role

        if role == "teacher":
            return redirect("teacher_dash")

        elif role == "student":
            return redirect("student_dash")

    return render(request, "login.html")
        
def signup(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        senroll = request.POST.get("enr_no")
        sstd = request.POST.get("sstd")
        mobno = request.POST.get("mobile")
        pmobno =request.POST.get("parent_mobile")
        address =request.POST.get("address")
        password =request.POST.get("password")
        confpassword =request.POST.get("confirm_password")

        if Signup.objects.filter(name=name).exists():
            return render (request,"signup.html",{"error":"Username already exist"})
        
        Signup.objects.create(
            name=name,
            email=email,
            senroll=senroll,
            sstd = sstd,
            mobno =mobno,
            pmobno=pmobno,
            address=address,
            password=password,
            confpassword=confpassword

        )
        return render (request,"signup.html",{"success":"Account created "})
    
    return render (request,"signup.html")

def student_dash(request):
    return render (request,"student_dash.html") 

def teacher_dash(request):
    return render (request,"teacher_dash.html") 

def activity(request):
    return render (request,"activity.html") 

def analytics(request):
    return render (request,"analytics.html") 

def attendance_sheet(request):
    return render (request,"attendance_sheet.html") 

def attendance(request):
    return render (request,"attendance.html") 

def marks(request):
    return render(request,"marks.html")

# 🔹 Fill Marks Page
def fill_marks(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        enrollment_no = request.POST.get("enrollment_no")
        standard = request.POST.get("standard")

        maths = int(request.POST.get("maths"))
        science = int(request.POST.get("science"))
        english = int(request.POST.get("english"))

        total = maths + science + english
        percentage = (total / 300) * 100

        # Grade Logic
        if percentage >= 90:
            grade = "A+ (EXCELLENT)"
        elif percentage >= 80:
            grade = "A (VERY GOOD)"
        elif percentage >= 70:
            grade = "B (GOOD)"
        elif percentage >= 60:
            grade = "C (AVERAGE)"
        elif percentage >= 50:
            grade = "D (PASS)"
        else:
            grade = "F (FAIL)"

        # Save to DB
        StudentMark.objects.create(
            student_name=student_name,
            enrollment_no=enrollment_no,
            standard=standard,
            maths=maths,
            science=science,
            english=english,
            total_marks=total,
            grade=grade
        )

        return redirect("view_marks")

    return render(request, "fill_marks.html")






    return render (request,"marks.html") 

def new_stu(request):

    if request.method == "POST":
        sname  = request.POST.get('sname')
        rollno = request.POST.get('rollno')
        enroll = request.POST.get('enroll')
        std    = request.POST.get('std')
        sec    = request.POST.get('sec')

        # Duplicate check
        if Student.objects.filter(enroll=enroll).exists():
            return render(request, "new_stu.html", {
                "error": "Student Already Exists"
            })

        # Save data
        Student.objects.create(
            sname=sname,
            rollno=rollno,
            enroll=enroll,
            std=std,
            sec=sec
        )

        return render(request, "new_stu.html", {
            "success": "Student Successfully Added"
        })

    # GET request
    return render(request, "new_stu.html")

def stu_sub(request):
    return render (request,"stu_sub.html") 

def students(request):
    students = Student.objects.all()
    return render (request,"students.html",{'students':students}) 

def view_marks(request):
    return render (request,"view_marks.html") 


def edit_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, "edit_student.html", {"student": student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')

def view_marks(request):
    marks = StudentMark.objects.all().order_by('student_name')

    return render(request, "view_marks.html", {
        "marks": marks
    })


def delete_marks(request, id):
    mark = get_object_or_404(StudentMark, id=id)
    mark.delete()
    return redirect('view_marks')


def add_activity(request):
    if request.method == "POST":

        activity_type = request.POST.get("activity_type")

        sports_name = None
        if activity_type == "sports":
            sports_name = request.POST.get("sports_name")

        StudentActivity.objects.create(
            student_name=request.POST.get("student_name"),
            enrollment_number=request.POST.get("enrollment"),
            school_name=request.POST.get("school_name"),
            standard=request.POST.get("standard"),
            activity_type=activity_type,
            sports_name=sports_name,
            activity_name=request.POST.get("activity_name"),
            description=request.POST.get("description"),
        )

        return redirect("student_dash")
    return render(request, "student_activity.html")



# analyser/views.py
from django.shortcuts import render
from .utils import ai_analyze_student_performance

def student_ai_performance_view(request):
    performance_data = ai_analyze_student_performance()
    return render(request, "student_ai_performance.html", {"performance_data": performance_data})

