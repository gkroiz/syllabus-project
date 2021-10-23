
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, LoginUser

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        # Checks if the username/password are valid and save it to the DB
        if form.is_valid():
            #form.save()  # Saves it to the Database
            # Log the user in the DB
            return redirect('login/login.html')
    else:
        form = CreateUserForm()
    return render(request, 'login/signup.html', {'form': form})  # send the form to the html

def login(request):
    if request.method == "POST":
        form = LoginUser(data=request.POST)
        if form.is_valid():
            print("GO TO HOME PAGE")
            #GO TO HOME PAGE
    else:
        form = LoginUser()
    return render(request, 'login/login.html', {'form': form})