from rest_framework import serializers
from .models import SpeechEx, MovementEx, TappingEx
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    speechex = serializers.PrimaryKeyRelatedField(many=True, queryset=SpeechEx.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'speechex']


class SpeechExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')


    # def create(self, validated_data):
    #     return super().create(validated_data)

    class Meta:
        model = SpeechEx
        fields = ['id', 'recording_id', 'recording_path', 'recording_file', 'patient_id']


class MovementExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = MovementEx
        fields = ['id', 'movement_id', 'movement_path', 'patient_id']


class TappingExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = TappingEx
        fields = ['id', 'tapping_id', 'tapping_path', 'patient_id']
