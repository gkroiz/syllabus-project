from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DeptInfo


# Create your views here.

def dept(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeptInfo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('submitted')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeptInfo()

    return render(request, 'dept_name/index.html', {'form': form})

# Basic template for submitted item
def submitted(request):
    return render(request, 'dept_name/submitted.html')
