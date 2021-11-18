"""syllabus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('login/', include('login.urls')),
    path('syllabus_form/', include('syllabus_form.urls')),
    path('profile/', include('faculty_profile.urls')),
    path('add/', include('synthesizew.urls')),

    #Needed for password reset. ONLY WORKS IF THEY ARE IN THE PROJECT URL AND NOT IN APP URL
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset/password_reset_complete.html'), name='password_reset_complete'),
]
