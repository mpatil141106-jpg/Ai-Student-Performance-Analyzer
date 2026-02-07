"""
URL configuration for stud_analyse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from analyser import views
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page),
    path('login/', views.login_view, name='login'),
    path('student_dash/',views.student_dash,name= 'student_dash'),
    path('teacher_dash/',views.teacher_dash,name='teacher_dash'),
    path('activity/',views.activity , name='activity'),
    path('analytics/',views.analytics, name='analytics'),
    path('attendance_sheet/',views.attendance_sheet,name='attendance_sheet'),
    path('attendance/',views.attendance,name='attendance'),
    path('marks/',views.marks,name='marks'),
    path('new_stu/',views.new_stu,name='new_stu'),
    path('signup/',views.signup,name='signup'),
    path('stu_sub',views.stu_sub,name='stu_sub'),
   
    path('view_marks/',views.view_marks,name='view_marks'),
    path('students/', views.students, name='students'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),

    path("fill-marks/", views.fill_marks, name="fill_marks"),

    path("delete-marks/<int:id>/", views.delete_marks, name="delete_marks"),
 
    path("add_activity/", views.add_activity, name="add_activity"),

    path('student_ai_performance/', views.student_ai_performance_view, name='student_ai_performance'),
]





