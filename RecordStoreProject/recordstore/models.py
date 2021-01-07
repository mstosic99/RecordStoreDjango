from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.IntegerField(validators=(MinValueValidator(1900), MaxValueValidator(2050)))
    image = models.URLField(default='')

    def __str__(self):
        return self.title


class UserHasRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
