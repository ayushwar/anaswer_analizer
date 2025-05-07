from django.shortcuts import render
from .models import StudentExam
import google.generativeai as genai
import re
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

# Initialize Google Gemini API
genai.configure(api_key="YOR API")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-pro")

QUESTION_MARKS = {
    "question_1": 5,
    "question_2": 5,
    "question_3": 5,
}

def create_prompt_for_single_answer(question, answer, max_marks):
    """
    Creates a prompt for evaluating a single student answer.
    """
    prompt = f"Evaluate the following student answer to the question: '{question}'.\n"
    prompt += f"Provide marks (out of {max_marks}) and brief feedback for the answer.\n\n"
    prompt += f"Answer: {answer}\n"
    prompt += "Provide marks and feedback."
    return prompt

def parse_llm_output(output):
    """
    Parses the LLM output to extract marks and feedback.
    Handles cases where LLM might not strictly follow "Marks:" and "Feedback:"
    """
    marks = None
    feedback = None
    lines = output.splitlines()
    for line in lines:
        if "marks" in line.lower():
            try:
                # Extract number even with surrounding text
                marks_value = re.search(r'(\d+\.?\d*)', line)
                if marks_value:
                    marks = float(marks_value.group(1))
            except ValueError:
                logger.warning(f"Could not parse marks from: {line}")
        elif "feedback" in line.lower():
            feedback_start = line.lower().find("feedback:") + len("feedback:")
            feedback = line[feedback_start:].strip()
            if not feedback:
                feedback = "" # handle empty feedback
    if marks is None:
        marks=0
    if feedback is None:
        feedback = "No feedback provided"
    return marks, feedback



def evaluate_question(question_number):
    """
    Evaluates student answers for a specific question using the LLM.

    Args:
        question_number (int): The question number to evaluate (1, 2, or 3).
    """
    question_field = f"question_{question_number}"
    answer_field = f"answer_{question_number}"
    marks_field = f"marks_{question_number}"
    feedback_field = f"feedback_{question_number}"
    max_marks = QUESTION_MARKS[question_field]

    students = StudentExam.objects.all()  # Get all students
    if not students.exists():
        logger.warning(f"No student records found for Question {question_number}.")
        return

    for student in students:
        question = getattr(student, question_field)
        answer = getattr(student, answer_field)

        if not question:
            logger.warning(f"Question text missing for {question_field} for {student.student_name}")
            continue

        if not answer:
            logger.info(f"Skipping {student.student_name} due to missing answer for {answer_field}.")
            continue

        prompt = create_prompt_for_single_answer(question, answer, max_marks)
        try:
            response = model.generate_content(prompt)
            output = response.text.strip()
            logger.info(f"LLM Output for {student.student_name} - Q{question_number}:\n{output}")
        except Exception as e:
            logger.error(f"Error generating LLM content for {student.student_name} - Q{question_number}: {e}", exc_info=True)
            continue

        marks, feedback = parse_llm_output(output)

        try:
            with transaction.atomic():
                setattr(student, marks_field, marks)
                setattr(student, feedback_field, feedback)
                student.save()
                logger.info(
                    f"Saved marks for {student.student_name} for Q{question_number}: Marks - {marks}, Feedback - {feedback}"
                )
        except Exception as db_error:
            logger.error(f"Database error: {db_error}", exc_info=True)



def run_evaluation(request):
    """
    Entry point to trigger the evaluation of all questions.
    """
    for i in range(1, 4):  # Evaluate each question (1, 2, and 3)
        evaluate_question(i)

    return render(request, "ai_evaluator/evaluate.html", {"message": "All questions evaluated!"})
