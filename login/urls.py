from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login')

]