from django.urls import path

from . import views

urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # routes from home page
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
]
