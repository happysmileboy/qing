from django.urls import path

from . import views

app_name = 'etc'



urlpatterns = [
    path('notice_list/', views.notice_list, name='notice_list'),
    path('notice_detail/<int:pk>/', views.notice_detail, name='notice_detail'),
    ]