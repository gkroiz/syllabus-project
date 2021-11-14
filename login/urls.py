from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'login'
urlpatterns = [


    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout_view'),
    path('', views.login_view, name='login')

]