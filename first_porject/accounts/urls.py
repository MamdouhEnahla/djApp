from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name ='accounts/login.html'), name='login'),
    path('update_password/', auth_views.PasswordChangeView.as_view(template_name ='accounts/update_password.html'), name='update_password'),
    path('updated_password/', auth_views.PasswordChangeDoneView.as_view(template_name ='accounts/updated_password.html'), name='updated_password'),



]