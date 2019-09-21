from django.urls import path, include
from .views import SpeechExListView, SpeechExRUDViewSet
from .views import UserDetail, UserList
from rest_framework import routers


urlpatterns = [
    path('speechex/', SpeechExListView.as_view(), name='speechex-list'),
    path('speechex/<int:pk>', SpeechExRUDViewSet.as_view(), name='speechex-detail'),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
