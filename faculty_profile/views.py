from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from faculty_profile.models import Profile, OfficeHours
from .forms import EditProfileForm


def index(request, user_id):
    # get the id of the logged in user if a user is logged in
    logged_in = False
    user = request.user
    if user.is_authenticated:
        logged_in = user.email.split('@')[0]

    profiles = Profile.objects.filter()

    no_profile = True
    for profile in profiles:
        # if corresponding user is found, retrieve office hours and change flag
        if user_id == profile.faculty_id:
            office_hours = OfficeHours.objects.filter(faculty=user_id)
            no_profile = False
            break

    # if there is NO user logged in and they are visiting a profile that DOES NOT exist
    if logged_in is False and no_profile:
        return render(request, 'faculty_profile/no_login_no_profile.html', context={'user_id': user_id})
    # if there is NO user logged in and they are visiting a profile that DOES exist
    elif not logged_in:
        return render(request, 'faculty_profile/no_login.html', context={'profile': profile,
                                                                         'office_hours': office_hours,
                                                                         'user_id': user_id})
    # if the logged in user is not visiting their own profile and the profile they're visiting DOES NOT exist
    elif user_id != logged_in and no_profile:
        return render(request, 'faculty_profile/not_ur_profile_no_profile.html', context={'user_id': user_id})
    # if the logged in user is not visiting their own profile, but the profile they're visiting exists
    elif user_id != logged_in:
        return render(request, 'faculty_profile/not_ur_profile.html', context={'profile': profile,
                                                                               'office_hours': office_hours,
                                                                               'user_id': user_id})
    # if the logged in user is visiting their own profile but they haven't created a profile yet
    elif no_profile:
        return render(request, 'faculty_profile/no_profile.html', context={'user_id': user_id})
    # if the logged user is on their own created profile
    else:
        return render(request, 'faculty_profile/index.html', context={'profile': profile,
                                                                      'office_hours': office_hours,
                                                                      'user_id': user_id})


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

                # get a list of extra fields
                fields_not_wanted = ['faculty_id', 'location', 'phone', 'extra_field_count']
                fields_given = list(form.get_fields().keys())
                extra_fields = list(set(fields_not_wanted) ^ set(fields_given))

                # save faculty profile
                form = form.save()

                # find and select the corresponding profile
                profile = list(Profile.objects.filter(faculty_id=request.POST.get('faculty_id')))[0]

                # save extra fields (office hours)
                for i in range(len(extra_fields)):
                    hours_given = request.POST.get(extra_fields[i])
                    office_hour = OfficeHours.objects.create(faculty=profile, date_time=hours_given)
                    office_hour.save()

                return redirect(reverse('faculty_profile:index', kwargs={'user_id': request.POST.get('faculty_id')}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditProfileForm()

    return render(request, 'faculty_profile/edit.html', {'form': form, 'user_id': user_id})


def syllabus(request, user_id):
    return HttpResponse('View will be connected to the syllabus app later')
