from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name ='accounts/login.html'), name='login'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name ='accounts/change_password.html'), name='change_password'),
    path('updated_password/', auth_views.PasswordChangeDoneView.as_view(template_name ='accounts/password_change_done.html'), name='password_change_done'),



]