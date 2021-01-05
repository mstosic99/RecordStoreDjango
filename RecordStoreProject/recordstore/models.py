from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Record(models.Model):
    name = models.CharField(default='', max_length=64)
    genre = models.CharField(default='', max_length=64)
    artist = models.CharField(default='', max_length=64)
    year = models.IntegerField(default=1900, validators=[MinValueValidator(1900), MaxValueValidator(2050)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserHasRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

