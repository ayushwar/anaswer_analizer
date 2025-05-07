# student_portal/views.py
from django.shortcuts import render, redirect
from .forms import StudentTestForm
from .models import StudentExam

# Static questions
QUESTIONS = [
    "1. What is Artificial Intelligence? (5 marks)",
    "2. Explain the working of Machine Learning algorithms.(5 marks)",
    "3. Differentiate between supervised and unsupervised learning.(5 marks)"
]

def test_view(request):
    if request.method == 'POST':
        form = StudentTestForm(request.POST)
        if form.is_valid():
            # Save to DB
            StudentExam.objects.create(
                student_name=form.cleaned_data['student_name'],
                roll_no=form.cleaned_data['roll_no'],
                question_1=QUESTIONS[0],
                answer_1=form.cleaned_data['answer_1'],
                question_2=QUESTIONS[1],
                answer_2=form.cleaned_data['answer_2'],
                question_3=QUESTIONS[2],
                answer_3=form.cleaned_data['answer_3']
            )
            print("✅ Student data saved successfully.")  # Optional debug
            return render(request, 'student_portal/success.html')
        else:
            print("❌ Form errors:", form.errors)  # Optional debug
    else:
        form = StudentTestForm()

    return render(request, 'student_portal/test_form.html', {
        'form': form,
        'questions': QUESTIONS
    })
