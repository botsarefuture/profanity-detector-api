# profanity_detector/serializers.py
from rest_framework import serializers

class ProfanityDetectionSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    language = serializers.CharField(required=False, default='en')
    profanity_detected = serializers.BooleanField(read_only=True)
