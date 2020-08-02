from django import forms
from .models import Student
from .models import Course
from .models import Result

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['cover','university','department','sid']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cover','course_no','course_title','credit_hours','level_term']
        #fields = '__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        # fields = ['name','author','description','price','available','catagory']
        fields = ['course','grade_point']
