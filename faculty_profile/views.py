from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faculty_profile.models import Profile


def index(request):
    profiles = Profile.objects.filter()
    return render(request, 'faculty_profile/index.html', context={'profiles': profiles})


def edit(request):
    return render(request, 'faculty_profile/edit.html', context={})


def syllabus(request):
    return HttpResponse('View will be connected to the syllabus app later')


def add(request):
    # if ID from form POST is the same as an ID that is already in the database, the existing entry will be modified
    # if ID is new, a new entry will be created
    profile_id = request.POST['ID']
    name = request.POST['name']
    email = request.POST['email']
    location = request.POST['location']
    phone = request.POST['phone']
    hours = request.POST['hours']
    profile_obj = Profile(ID=profile_id, name=name, email=email, location=location, phone=phone, hours=hours)
    profile_obj.save()
    return HttpResponseRedirect(reverse('faculty_profile:index'))
