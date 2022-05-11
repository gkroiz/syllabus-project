from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('search', views.search, name='search')
]
