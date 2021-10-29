from django.urls import path

from . import views

app_name = 'faculty_profile'
urlpatterns = [
    # profile page(s)
    path('', views.index, name='index'),
    path('<int:profile_id>/', views.profile, name='profile'),
    path('<int:profile_id>/edit/', views.edit, name='edit')
]
