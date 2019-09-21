from rest_framework import serializers
from .models import SpeechEx
from django.contrib.auth.models import User


class SpeechExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = SpeechEx
        fields = ['recording_id', 'recording_path', 'patient_id']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    speechex = serializers.PrimaryKeyRelatedField(many=True, queryset=SpeechEx.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'speechex']
