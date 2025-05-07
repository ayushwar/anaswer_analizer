# student_portal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test_form'),
]
