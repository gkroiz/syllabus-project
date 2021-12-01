from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from synthesizew.models import Syllabus


# Create your views here.
def index(request):
    return render(request, 'lookup/index.html', context={})


def results(request):
    course_title = request.GET.get('title_search')
    search_results = Syllabus.objects.filter(title__contains=course_title)
    context = {
        "search_results": search_results
    }
    return render(request, 'lookup/index.html', context=context)
