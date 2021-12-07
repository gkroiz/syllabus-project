from django.shortcuts import render
from synthesizew.models import Syllabus


# Create your views here.
def index(request):
    return render(request, 'lookup/index.html', context={})


def results(request):
    search_by = request.GET.get('dropdown')
    search_results = {}
    if search_by == 'course_title':
        course_title = request.GET.get('search_bar')
        search_results = Syllabus.objects.filter(title__contains=course_title)
    elif search_by == 'instructor_name':
        instructor_name = request.GET.get('search_bar')
        search_results = Syllabus.objects.filter(instructor_name__contains=instructor_name)
    elif search_by == 'course_time':
        course_time = request.GET.get('search_bar')
        search_results = Syllabus.objects.filter(course_time__contains=course_time)
    context = {
        "search_results": search_results
    }
    return render(request, 'lookup/index.html', context=context)
