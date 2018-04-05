from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('guideline/<int:pk>/', views.guideline, name='guideline'),
    path('apply/<int:pk>/', views.apply_mentoring, name='apply_mentoring'),
    path('reserved/<int:pk>/',views.mentoring_reserved, name='mentoring_reserved'),
    path('my_reservation/<str:username>/', views.my_reservation, name='my_reservation')
]