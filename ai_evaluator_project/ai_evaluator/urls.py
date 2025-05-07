from django.urls import path
from . import views

urlpatterns = [
    path('', views.run_evaluation, name='evaluate'),
    # path('test_save/', views.test_save, name='test_save'),
]
