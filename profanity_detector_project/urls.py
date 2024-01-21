# profanity_detector_project/urls.py
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Profanity Detector API",
        default_version='v1',
        description="An API for detecting profanity in text.",
        terms_of_service="https://your-terms-of-service-url.com/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# profanity_detector_project/urls.py
from drf_yasg import openapi

openapi_info = openapi.Info(
    title="Profanity Detector API",
    default_version='v1',
    description="An API for detecting profanity in text.",
    terms_of_service="https://your-terms-of-service-url.com/",
    contact=openapi.Contact(email="your-email@example.com"),
    license=openapi.License(name="MIT License"),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profanity_detector.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^$', RedirectView.as_view(url='/swagger/', permanent=True)),
]
