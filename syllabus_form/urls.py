from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.course),
    path('pdf_view', views.pdf_view)
]

