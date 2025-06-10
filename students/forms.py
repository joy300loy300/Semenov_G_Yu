from django import forms
from .models import Group, Student, Grade


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'group']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']
