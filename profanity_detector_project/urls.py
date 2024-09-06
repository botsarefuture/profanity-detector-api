from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

openapi_info = openapi.Info(
    title="Profanity Detector API",
    default_version="v1",
    description="An API for detecting profanity in text.",
    contact=openapi.Contact(email="vuoreol@gmail.com"),
    license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("profanity_detector.urls")),
    path(
        "swagger<str:format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^$", RedirectView.as_view(url="/swagger/", permanent=True)),
]

# Add servers
schema_view._servers = [
    {"url": "http://localhost:8000", "description": "Local development server"},
    {"url": "https://api.profanity.luova.club", "description": "Production server"},
    # Add more servers as needed
]
