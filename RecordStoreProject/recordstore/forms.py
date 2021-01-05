from django.forms import ModelForm
from .models import Record, UserHasRecord
from django.contrib.auth.models import User


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'genre', 'artist', 'year']


class UserHasRecordForm(ModelForm):
    class Meta:
        model = UserHasRecord
        fields = ['recordId', 'userId']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
