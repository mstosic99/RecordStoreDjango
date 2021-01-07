from django.contrib import admin
from .models import Record, UserHasRecord

admin.site.register(Record)
admin.site.register(UserHasRecord)
