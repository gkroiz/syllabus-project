from django.urls import path

from . import views

app_name = 'dept_info'
urlpatterns = [
    # home page
    path('', views.dept, name='dept'),
    path('submitted', views.dept, name='submitted'),
]
