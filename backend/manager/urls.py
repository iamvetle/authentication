from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth") # The built in login view that DRF provides
    # path("register/", views.register, name="register") # Registration - not made
]