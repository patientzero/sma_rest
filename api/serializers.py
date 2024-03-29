from rest_framework import serializers
from .models import SpeechEx, MovementEx, TappingEx, Metadata, Medication
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    speech_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=SpeechEx.objects.all())
    tapping_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=TappingEx.objects.all())
    movement_ex = serializers.PrimaryKeyRelatedField(many=True, queryset=MovementEx.objects.all())
    medication = serializers.PrimaryKeyRelatedField(many=True, queryset=Medication.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'speech_ex', 'tapping_ex', 'movement_ex', 'medication']


class SpeechExSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = SpeechEx
        fields = ['id', 'recording_id', 'recording_path', 'recording_file', 'task_kind', 'is_done', 'patient_id']


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


class MetadataSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = Metadata
        fields =['id', 'phone_number', 'gender', 'birthday', 'smoker', 'year_diag', 'other_disorder', 'educational_level', 'weight', 'height', 'session', 'patient_id']


class MedicationSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='patient_id.username')

    class Meta:
        model = Medication
        fields = ['id', 'patient_id', 'medication_name', 'medication_dose', 'medication_time']
