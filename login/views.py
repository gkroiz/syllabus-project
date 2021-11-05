from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, UserCreationForm


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # Checks if the username/password are valid and save it to the DB
        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})  # send the form to the html


def login(request):
    return render(request, 'login/login.html')


def index(request):
    return render(request, 'login/index.html')
