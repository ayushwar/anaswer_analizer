# student_portal/models.py

from django.db import models

class StudentExam(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)

    question_1 = models.TextField()
    answer_1 = models.TextField(blank=True, null=True)
    marks_1 = models.FloatField(blank=True, null=True)
    feedback_1 = models.TextField(blank=True, null=True)

    question_2 = models.TextField()
    answer_2 = models.TextField(blank=True, null=True)
    marks_2 = models.FloatField(blank=True, null=True)
    feedback_2 = models.TextField(blank=True, null=True)

    question_3 = models.TextField()
    answer_3 = models.TextField(blank=True, null=True)
    marks_3 = models.FloatField(blank=True, null=True)
    feedback_3 = models.TextField(blank=True, null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.roll_no})"
