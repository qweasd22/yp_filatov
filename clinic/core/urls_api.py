from rest_framework.routers import DefaultRouter

from django.urls import path
from .views_api import *

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'visits', VisitViewSet)

urlpatterns = router.urls