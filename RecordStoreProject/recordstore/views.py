from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Record


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html', {'page_title': 'Records'})
    else:
        return redirect('recordstore:records')


def record(request, id):
    return render(request, 'record.html')


def records(request):
    tmp = Record.objects.all()
    return render(request, 'records.html', {'records':tmp})


def new(request):
    return render(request, 'new.html')


def edit(request, id):
    return render(request, 'edit.html')
