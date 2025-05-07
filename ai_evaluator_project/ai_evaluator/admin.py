from django.contrib import admin
from .models import StudentExam

@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no', 'marks_1', 'feedback_1', 'marks_2', 'feedback_2', 'marks_3', 'feedback_3', 'submitted_at')
    search_fields = ('student_name', 'roll_no')