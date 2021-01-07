from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Record, UserHasRecord
from django.db import models


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'artist', 'genre', 'year', 'image']


class UserHasRecordForm(ModelForm):
    class Meta:
        model = UserHasRecord
        fields = ['user', 'record']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
