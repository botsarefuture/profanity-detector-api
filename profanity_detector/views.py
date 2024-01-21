from rest_framework.decorators import api_view
from rest_framework.response import Response
from profane_detector import ProfaneDetector

profane_detector = ProfaneDetector()

@api_view(['POST'])
def detect_profanity(request):
    if request.method == 'POST':
        try:
            # Check if 'text' parameter is present in the request data
            text_to_detect = request.data['text']
            
            # Validate that 'text' parameter is not empty
            if not text_to_detect.strip():
                raise ValueError("'text' parameter cannot be empty.")

            language = request.data.get('language', 'en')  # Default to English if language is not specified
            is_profane = profane_detector.detect_api(language, text_to_detect)

            response_data = {
                'text': text_to_detect,
                'language': language,
                'profanity_detected': is_profane,
            }

            return Response(response_data)
        except KeyError:
            return Response({'error': "Missing 'text' parameter in the request data."}, status=400)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    else:
        return Response({'error': 'Invalid request method'}, status=405)
