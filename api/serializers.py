from rest_framework import serializers
from .models import SpeechEx, MovementEx, TappingEx
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    speech_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=SpeechEx.objects.all())
    tapping_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=TappingEx.objects.all())
    movement_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=MovementEx.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'speech_ex', 'tapping_ex', 'movement_ex']


class SpeechExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = SpeechEx
        fields = ['id', 'recording_id', 'recording_path', 'recording_file', 'patient_id']


class MovementExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = MovementEx
        fields = ['id', 'movement_id', 'movement_path', 'movement_file', 'patient_id']


class TappingExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = TappingEx
        fields = ['id', 'tapping_id', 'tapping_path', 'tapping_file', 'patient_id']
