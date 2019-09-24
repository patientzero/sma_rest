from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import SpeechEx, Medication

admin.site.register(SpeechEx)
admin.site.register(Medication)
