from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=155, required=True, widget=forms.EmailInput())
    
    class Meta:
        model = User 
        fields ={'username', 'password2','email','password1'  }


