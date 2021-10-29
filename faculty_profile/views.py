from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'faculty_profile/index.html', context={})


def edit(request):
    return render(request, 'faculty_profile/edit.html', context={})
