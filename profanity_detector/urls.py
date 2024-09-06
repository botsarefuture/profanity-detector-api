# profanity_detector/urls.py
from django.urls import path
from .views import detect_profanity

urlpatterns = [
    path("detect-profanity/", detect_profanity, name="detect_profanity"),
]
