from django.db import models
from rest_framework import serializers

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class SpeechEx(models.Model):
    # unique recording id
    recording_id = models.CharField(max_length=255, null=False)
    # path to recording
    recording_path = models.CharField(max_length=255, null=False)
    # unique patient id, usually based on the android device id and / or email address
    patient_id = models.ForeignKey('auth.User', related_name='speechex', on_delete=models.PROTECT)

    # Can be overridden, not needed here
    # def save(self, *args, **kwargs):
    #     super(SpeechEx, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.recording_id, self.recording_path, self.patient_id)
