from django.urls import path

from . import views

urlpatterns = [
    # profile page(s)
    path('', views.index, name='index'),
    path('<int:profile_id>/', views.index, name='profile'),
    path('<int:profile_id>/edit/', views.index, name='profile_edit')
]
