from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import SpeechEx
from rest_framework import generics, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import SpeechExSerializer, UserSerializer
from .serializers import MovementExSerializer, MovementEx
from .serializers import TappingExSerializer, TappingEx
from .serializers import MetadataSerializer, Metadata
from .serializers import MedicationSerializer, Medication


from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser

from .tasks import celery_test, celery_test2


@parser_classes([MultiPartParser])
class SpeechExCreateView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SpeechEx.objects.all()
    serializer_class = SpeechExSerializer

    def create(self, request, *args, **kwargs):
        
        request.data._mutable = True
        request.data.update({"patient_id": request.user.id})

        return super().create(request, *args, **kwargs)


@parser_classes([MultiPartParser])
class MovementExCreateView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MovementEx.objects.all()
    serializer_class = MovementExSerializer

    def create(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data.update({"patient_id": request.user.id})

        return super().create(request, *args, **kwargs)


@parser_classes([MultiPartParser])
class TappingExCreateView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TappingEx.objects.all()
    serializer_class = TappingExSerializer

    def create(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data.update({"patient_id": request.user.id})

        return super().create(request, *args, **kwargs)


@parser_classes([MultiPartParser])
class MedicationCreateView(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    def create(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data.update({"patient_id": request.user.id})

        # Celery example tests
        celery_test.delay()
        celery_test2.delay(8, 9)

        return super().create(request, *args, **kwargs)


class MetadataCreateView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# TODO: Check file input, if exists, else correct status code
# TODO: make location configurable, default location == MEDIA_ROOT, in fs.save realtive to MEDIA_ROOT
# fs = FileSystemStorage(location=wavfolder)  # todo: avoid overwriting
## TODO determine file name according to input data/user, something like: PA_ID_EX_ID_EXName_TIME_DATE, if serializer not valid delte file
