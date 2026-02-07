from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='home'),  # root URL goes to login_page
    path('login/', views.login_view, name='login'),
    path('student_dash/', views.student_dash, name='student_dash'),
    path('teacher_dash/', views.teacher_dash, name='teacher_dash'),
    path('activity/', views.activity, name='activity'),
    path('analytics/', views.analytics, name='analytics'),
    path('attendance_sheet/', views.attendance_sheet, name='attendance_sheet'),
    path('attendance/', views.attendance, name='attendance'),
    path('marks/', views.marks, name='marks'),
    path('new_stu/', views.new_stu, name='new_stu'),
    path('signup/', views.signup, name='signup'),
    path('stu_sub/', views.stu_sub, name='stu_sub'),
    path('view_marks/', views.view_marks, name='view_marks'),
    path('students/', views.students, name='students'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('fill-marks/', views.fill_marks, name='fill_marks'),
    path('delete-marks/<int:id>/', views.delete_marks, name='delete_marks'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('student_performance/', views.student_performance, name='student_performance'),
]
