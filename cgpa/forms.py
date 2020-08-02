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
        fields = ['course_no','credit_hours','course_title','level_term']
        #fields = '__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        # fields = ['name','author','description','price','available','catagory']
        fields = ['course','grade_point']
