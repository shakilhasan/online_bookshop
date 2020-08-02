from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    cover= models.ImageField(upload_to='images/cgpa/', null=True,blank=True,default='images/cgpa/student_default.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    #user = models.ForeignKey(User,on_delete=models.CASCADE,)
    university = models.CharField(max_length=100,)
    department = models.CharField(max_length=100,)
    sid = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Course(models.Model):
    cover= models.ImageField(upload_to='images/cgpa/', null=True, blank=True, default='images/cgpa/course_default.jpeg')
    university = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,)
    course_no = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100, null=True)
    credit_hours = models.FloatField()
    level_term = models.IntegerField()

    def __str__(self):
        return str(self.course_no)

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)
    grade_point = models.FloatField()

    def __str__(self):
        return str(self.id)
