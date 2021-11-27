from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from faculty_profile.models import Profile
from .forms import EditProfileForm


def index(request, user_id):
    profiles = Profile.objects.filter()

    no_profile = True
    for profile in profiles:
        if user_id == profile.ID:
            no_profile = False
            break

    # create another if statement to see if the user is authorized to edit the profile or
    # should be redirected to a template that cannot edit the profile
    if no_profile:
        return render(request, 'faculty_profile/no_profile.html', context={'user_id': user_id})
    else:
        return render(request, 'faculty_profile/index.html', context={'profile': profile, 'user_id': user_id})


def edit(request, user_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EditProfileForm(request.POST, extra=request.POST.get('extra_field_count'), use_required_attribute=False)
        if 'add' in request.POST:
            print('you pressed add button')
            print('count: ' + str(request.POST.get('extra_field_count')))
            return render(request, 'faculty_profile/edit.html', {'form': form, 'user_id': user_id})
        if 'submit' in request.POST:
            print('you pressed submit button')
            if form.is_valid():
                print("valid!")
                print(form.get_fields())

                form = form.save()

                return redirect(reverse('faculty_profile:index', kwargs={'user_id': request.POST.get('ID')}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditProfileForm()

    return render(request, 'faculty_profile/edit.html', {'form': form, 'user_id': user_id})


def syllabus(request, user_id):
    return HttpResponse('View will be connected to the syllabus app later')
