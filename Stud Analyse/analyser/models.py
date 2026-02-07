from django.db import models

# Create your models here.
class User (models.Model):
    uname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=[
            ('student','Student'),
            ('teacher','Teacher'),
        ],
        default='student'
    )

class Student(models.Model):
    sname = models.CharField(max_length=100)
    rollno = models.IntegerField()
    enroll = models.IntegerField()
    std = models.CharField(max_length=100)
    sec = models.CharField()

class Signup (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sstd = models.IntegerField(max_length=100)
    senroll = models.IntegerField(max_length=100)
    mobno = models.IntegerField(max_length=12)
    pmobno = models.IntegerField(max_length=12)
    address = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    confpassword =  models.CharField(max_length=100)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]
    )
    attended_days = models.IntegerField(default=0)
    total_days = models.IntegerField(default=0)

    def percentage(self):
        if self.total_days == 0:
            return 0
        return round((self.attended_days / self.total_days) * 100)
    
    from django.db import models

class StudentMark(models.Model):

    STANDARD_CHOICES = [
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    student_name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=50, unique=True)
    standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)

    maths = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    english = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField()
    grade = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.enrollment_no})"
    
    from django.db import models

from django.db import models

class StudentActivity(models.Model):

    ACTIVITY_TYPE_CHOICES = [
        ('sports', 'Sports'),
        ('drawing', 'Drawing'),
        ('dance', 'Dance'),
        ('music', 'Music'),
        ('drama', 'Drama'),
    ]

    SPORTS_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('badminton', 'Badminton'),
        ('table_tennis', 'Table Tennis'),
        ('volleyball', 'Volleyball'),
        ('swimming', 'Swimming'),
        ('long_jump', 'Long Jump'),
    ]

    student_name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=50)
    school_name = models.CharField(max_length=150)
    standard = models.CharField(max_length=20)

    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPE_CHOICES
    )

    sports_name = models.CharField(
        max_length=30,
        choices=SPORTS_CHOICES,
        blank=True,
        null=True
    )

    activity_name = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.activity_type}"