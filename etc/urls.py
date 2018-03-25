from django.urls import path

from . import views

app_name = 'etc'



urlpatterns = [
    path('notice_list/', views.notice_list, name='notice_list'),
    path('notice_detail/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('charge_info/', views.charge_info, name='charge_info'),
    path('inquiry/', views.inquiry, name='inquiry'),
    ]