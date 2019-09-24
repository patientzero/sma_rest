from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import SpeechEx, Metadata, Medication

admin.site.register(SpeechEx)
admin.site.register(Metadata)
admin.site.register(Medication)