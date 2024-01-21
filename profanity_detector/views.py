# profanity_detector/views.py
"""
OpenAPI (Swagger) Documentation
... (same as before)
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profane_detector import ProfaneDetector
from .serializers import ProfanityDetectionSerializer
from drf_yasg.utils import swagger_auto_schema

profane_detector = ProfaneDetector()

@swagger_auto_schema(
    method='post',
    request_body=ProfanityDetectionSerializer,
    responses={
        200: ProfanityDetectionSerializer(many=False),
        400: "Bad request - Missing 'text' parameter or empty text.",
        405: "Invalid request method.",
        500: "Internal server error."
    }
)
@api_view(['POST'])
def detect_profanity(request):
    """
    Detect profanity in the provided text.

    Parameters:
    - text (str): Text to be checked for profanity.
    - language (str, optional): Language of the text (default is English).

    Returns:
    - 200: Successful response.
    - 400: Bad request - Missing 'text' parameter or empty text.
    - 405: Invalid request method.
    - 500: Internal server error.
    """
    if request.method == 'POST':
        try:
            # Use the serializer to validate and deserialize the request data
            serializer = ProfanityDetectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            text_to_detect = serializer.validated_data['text']
            language = serializer.validated_data.get('language', 'en')  # Default to English if language is not specified

            # Validate that 'text' parameter is not empty
            if not text_to_detect.strip():
                raise ValueError("'text' parameter cannot be empty.")

            is_profane = profane_detector.detect_api(language, text_to_detect)

            response_data = {
                'text': text_to_detect,
                'language': language,
                'profanity_detected': is_profane,
            }

            return Response(response_data)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    else:
        return Response({'error': 'Invalid request method'}, status=405)
