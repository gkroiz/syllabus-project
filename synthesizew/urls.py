from django.urls import path
from . import views


app_name = 'synthesizew'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.add, name='add'),
]
