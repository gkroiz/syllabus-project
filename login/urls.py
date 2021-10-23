from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url('', views.login, name='login')
    #path('', views.login, name='login'),

    #path('signup/', views.signup, name='signup')


]