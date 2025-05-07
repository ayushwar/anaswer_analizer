# student_portal/admin.py
from django.contrib import admin
from .models import StudentExam

@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no', 'submitted_at')  # Add fields to display in admin
    search_fields = ('student_name', 'roll_no')  # Allows searching by student name or roll number
    list_filter = ('submitted_at',)  # Optional: Filters the data by submission time
