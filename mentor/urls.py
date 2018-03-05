from django.urls import path

from . import views

app_name = 'mentor'



urlpatterns = [
    path('', views.consult_main, name='consult_main'),
    path('search', views.search_univ_mentor, name='search_univ_mentor')
]