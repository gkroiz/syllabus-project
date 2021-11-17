from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


from .forms import AccountAuthenticationForm, UserCreationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.



def password_reset_request(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "login/password_reset/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('password_reset_done')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="login/password_reset/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            #login(request, account)
            return redirect('login:login')
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
        return redirect('faculty_profile:index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('faculty_profile:index')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form

    return render(request, 'login/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    return render(request, 'login/homepage.html')
