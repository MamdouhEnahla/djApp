from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()
    context ={
        'form': form,
    }
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            user =form.save()
            auth_login(request, user)
            return redirect('index')
    
    return render(request, 'accounts/signup.html', context)