from django import forms
from .models import Student

class TaskForm(forms.ModelForm):##To add without input field##
    class Meta:
        model = Student
        fields = ['name', 'email', 'dob']


        fields = ['name', 'email', 'dob']
