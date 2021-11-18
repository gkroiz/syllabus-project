from django.urls import path

from . import views

app_name = 'dept_info'
urlpatterns = [
    # dept page
    path('', views.dept, name='dept'),
    path('submitted', views.submitted, name='submitted'),
]
