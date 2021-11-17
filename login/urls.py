from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'
urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('', views.login_view, name='login'),

    path("password_reset/", views.password_reset_request, name="password_reset"),


]