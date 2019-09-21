from django.test import TestCase

# Create your tests here.


from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import SpeechEx
from .serializers import SpeechExSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_speech(recording_id="", patient_id=""):
        if recording_id != "" and patient_id != "":
            SpeechEx.objects.create(recording_id=recording_id, patient_id=patient_id)

    def setUp(self):
        # add test data
        self.create_speech("abc", "patient_01")
        self.create_speech("def", "patient_02")
        self.create_speech("ghi", "patient_03")
        self.create_speech("jkl", "patient_04")


class GetAllSpeechTest(BaseViewTest):

    def test_get_all_speech(self):
        """
        This test ensures that all speech exercises are added in the setUp method
        exist when we make a GET request to the speech/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("speech-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = SpeechEx.objects.all()
        serialized = SpeechExSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)