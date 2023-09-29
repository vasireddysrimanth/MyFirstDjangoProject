from django.shortcuts import render

# Create your views here.


def task1(request):
    return render(request, 'myapp/task1.html')
