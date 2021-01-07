from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .forms import RecordForm, UserHasRecordForm, SignUpForm
from .models import Record, UserHasRecord


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Record Store'})
    else:
        return redirect('recordstore:records')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recordstore:records')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@login_required
def add_wish(request, id):
    a = UserHasRecord()
    rec = Record.objects.get(id=id)
    a.record = rec
    a.user = request.user
    tmp = list(UserHasRecord.objects.filter(user=request.user))
    has = False
    for t in tmp:
        if t.record == a.record:
            has = True
    if not has:
        a.save()

    return redirect('recordstore:records')


@login_required
def wishlist(request):
    tmp = UserHasRecord.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'records': tmp})


@login_required
def records(req):
    tmp = Record.objects.order_by('title').all()
    return render(req, 'records.html', {'records': tmp})


@login_required
def record(req, id):
    tmp = get_object_or_404(Record, id=id)
    return render(req, 'record.html', {'record': tmp, 'page_title': tmp.title})


@permission_required('recordstore.change_record')
def edit(req, id):
    if req.method == 'POST':
        form = RecordForm(req.POST)

        if form.is_valid():
            a = Record.objects.get(id=id)
            a.image = form.cleaned_data['image']
            a.title = form.cleaned_data['title']
            a.artist = form.cleaned_data['artist']
            a.genre = form.cleaned_data['genre']
            a.year = form.cleaned_data['year']
            a.save()
            return redirect('recordstore:records')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Record.objects.get(id=id)
        form = RecordForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('recordstore.add_record')
def new(req):
    if req.method == 'POST':
        form = RecordForm(req.POST)

        if form.is_valid():
            a = Record(image=form.cleaned_data['image'], title=form.cleaned_data['title'],
                       artist=form.cleaned_data['artist'],
                       genre=form.cleaned_data['genre'], year=form.cleaned_data['year'])
            a.save()
            return redirect('recordstore:records')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = RecordForm()
        return render(req, 'new.html', {'form': form})


def delete(req, id):
    Record.objects.filter(id=id).delete()
    return redirect('recordstore:records')
