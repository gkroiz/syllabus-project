from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup')
]
