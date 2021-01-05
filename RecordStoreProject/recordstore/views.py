from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Welcome')


def hello(request):
    return render(request, 'recordstore/hello.html')


