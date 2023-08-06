## INSIDE ROOT SETTINGS.PY

INSTALLED_APPS = [
    # ...
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    # ...
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Replace with your frontend server's URL
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

## INSIDE MANAGER URLS.PY

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # other paths...
]