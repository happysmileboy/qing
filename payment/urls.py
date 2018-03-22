from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('guideline/', views.guideline, name='guideline'),
    path('apply/', views.apply_mentoring, name='apply_mentoring'),
]