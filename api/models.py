from django.db import models
from rest_framework import serializers

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class SpeechEx(models.Model):
    # unique recording id
    recording_id = models.CharField(max_length=255, null=False)
    # path to recording
    recording_path = models.CharField(max_length=255, blank=True) # custom validator moeglich
    recording_file = models.FileField(storage=FileSystemStorage(location='speech_ex/'), null=False, default='/', )
    # filefield with local storage backend
    # unique patient id, usually based on the android device id and / or email address
    patient_id = models.ForeignKey('auth.User', related_name='speechex', on_delete=models.PROTECT)
    #filefield with local storage backend
    # Can be overridden, not needed here
    # def save(self, *args, **kwargs):
    #     super(SpeechEx, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.recording_id, self.recording_path, self.patient_id)


class MovementEx(models.Model):
    # unique track id
    movement_id = models.CharField(max_length=255, null=False)
    # path to recording
    movement_path = models.CharField(max_length=255, null=False)
    movement_file = models.FileField(storage=FileSystemStorage(location='movement_ex/'), null=False, default='/', )

    # unique patient id, usually based on the android device id and / or email address
    patient_id = models.ForeignKey('auth.User', related_name='movementex', on_delete=models.PROTECT)

    # Can be overridden, not needed here
    # def save(self, *args, **kwargs):
    #     super(SpeechEx, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.movement_id, self.movement_path, self.patient_id)


class TappingEx(models.Model):
    # unique tapping exercise id
    tapping_id = models.CharField(max_length=255, null=False)
    # path to recording
    tapping_path = models.CharField(max_length=255, null=False)
    # unique patient id, usually based on the android device id and / or email address
    patient_id = models.ForeignKey('auth.User', related_name='tappingex', on_delete=models.PROTECT)
    tapping_file = models.FileField(storage=FileSystemStorage(location='tapping_ex/'), null=False, default='/', )

    # Can be overridden, not needed here
    # def save(self, *args, **kwargs):
    #     super(SpeechEx, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.tapping_id, self.tapping_path, self.patient_id)


class Metadata (models.Model):

    phone_number = models.CharField(max_length=30)

    gender = models.CharField(max_length=30)

    birthday = models.IntegerField()

    smoker = models.BooleanField()

    year_diag = models.IntegerField(default='0')

    other_disorder = models.CharField(max_length=250, default='empty')

    educational_level = models.IntegerField()

    weight = models.IntegerField(default='0')

    height = models.IntegerField(default='0',)

    session = models.IntegerField()

    patient_id = models.ForeignKey('auth.User', related_name='metadata', on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}- {} - {} - {}".format(self.id, self.phone_number, self.gender, self.birthday, self.smoker, self.year_diag, self.other_disorder, self.educational_level, self.weight, self.height, self.session, self.patient_id)