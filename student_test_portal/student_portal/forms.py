# student_portal/forms.py
from django import forms

class StudentTestForm(forms.Form):
    student_name = forms.CharField(max_length=100, label="Student Name")
    roll_no = forms.CharField(max_length=20, label="Roll Number")

    answer_1 = forms.CharField(widget=forms.Textarea, label="Answer 1")
    answer_2 = forms.CharField(widget=forms.Textarea, label="Answer 2")
    answer_3 = forms.CharField(widget=forms.Textarea, label="Answer 3")
