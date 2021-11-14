from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # routes from home page
    path('search/', views.search, name='search'),
]
