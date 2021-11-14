from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('', views.login_view, name='login')

]