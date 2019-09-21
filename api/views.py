from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import SpeechEx
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpeechExSerializer, UserSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from django.core.files.storage import FileSystemStorage
from django.conf import settings



class SpeechExListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        snippets = SpeechEx.objects.all()
        serializer = SpeechExSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO: Check file input, if exists, else correct status code
        wav = request.data['data']
        wavfolder = 'speech_ex/'  # TODO: make location configurable, default location == MEDIA_ROOT, in fs.save realtive to MEDIA_ROOT
        fs = FileSystemStorage(location=wavfolder)  # todo: avoid overwriting

        filename = fs.save(wav.name, wav) # TODO determine file name according to input data/user, something like: PA_ID_EX_ID_EXName_TIME_DATE, if serializer not valid delte file
        request.data['recording_path'] = '{}/{}'.format(wavfolder, filename)
        request.data['patient_id'] = request.user.id
        serializer = SpeechExSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(patient_id=self.request.user)


# ViewSets define the view behavior.
class SpeechExRUDViewSet(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = SpeechEx.objects.all()
    serializer_class = SpeechExSerializer

    def get_object(self, pk):
        try:
            return SpeechEx.objects.get(pk=pk)
        except SpeechEx.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpeechExSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SpeechExSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#
# class UserListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = User.objects.all()
#         serializer = UserSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # ViewSets define the view behavior.
# class UserRUDViewSet(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = UserSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
