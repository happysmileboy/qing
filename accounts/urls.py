from django.urls import path

from . import views
# Create your views here.




app_name = 'accounts'


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='account_login'),
    path('signup/', views.MySignupView.as_view(), name='account_signup'),
    path('logout/', views.Logout, name="account_logout"),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='account_reset_password'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('confirm/', views.confirm_email, name='confirm_email'),
    path('confirm/sent/', views.email_confirm_sent, name='email_confirm_sent'),
]