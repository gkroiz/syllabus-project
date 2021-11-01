from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, LoginUser


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # Checks if the username/password are valid and save it to the DB
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log the user in the DB
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})  # send the form to the html


def login(request):
    if request.method == "POST":
        form = LoginUser(data=request.POST)
        if form.is_valid():
            print("GO TO HOME PAGE")
            # GO TO HOME PAGE
    else:
        form = LoginUser()
    return render(request, 'login/login.html', {'form': form})


def index(request):
    return render(request, 'login/index.html')
