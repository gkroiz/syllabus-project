from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', context={})


def login(request):
    return HttpResponse("View will be connected to the login app later")


def search(request):
    return HttpResponse("View will be connected to the search app later")
