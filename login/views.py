from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AccountAuthenticationForm, UserCreationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:  # Get request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'login/signup.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form

    return render(request, 'login/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'login/index.html')