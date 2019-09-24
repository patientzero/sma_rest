from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SpeechExCreateView, MovementExCreateView
from .views import TappingExCreateView, MetadataCreateView, MedicationCreateView
from .views import UserDetail, UserList

router = DefaultRouter()
router.register(r'', SpeechExCreateView)
movement_router = DefaultRouter()
movement_router.register(r'', MovementExCreateView)
tapping_router = DefaultRouter()
tapping_router. register(r'', TappingExCreateView)
metadata_router = DefaultRouter()
metadata_router. register(r'', MetadataCreateView)
medication_router = DefaultRouter()
medication_router.register(r'', MedicationCreateView)

urlpatterns = [
    path('speechex/', include(router.urls)),
    path('movementex/', include(movement_router.urls)),
    path('tappingex/', include(tapping_router.urls)),
    path('metadata/', include(metadata_router.urls)),
    path('medication/', include(medication_router.urls)),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
