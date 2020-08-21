from django import forms
from .models import Student
from .models import Course
from .models import Result

TITLE_CHOICES = [
('11', 11),
('12', 12),
('21', 21),
('22', 22),
('31', 31),
('32', 32),
('41', 41),
('42', 42),
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['cover','university','department','sid']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        level_term = forms.IntegerField(
                widget=forms.Select(choices=TITLE_CHOICES),
            )
        fields = ['cover','course_no','course_title','credit_hours','level_term']
        #fields = '__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        # fields = ['name','author','description','price','available','catagory']
        fields = ['course','grade_point']
