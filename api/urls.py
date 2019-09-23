from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SpeechExListView, SpeechExRUDViewSet, SpeechExView
from .views import UserDetail, UserList
from rest_framework import routers

router = DefaultRouter()
router.register(r'', SpeechExView)

urlpatterns = [
    path('speech/', include(router.urls)),
    path('speechex/', SpeechExListView.as_view(), name='speechex-list'),
    path('speechex/<int:pk>', SpeechExRUDViewSet.as_view(), name='speechex-detail'),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
