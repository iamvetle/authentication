from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CurrentUserView, RegisterUserView

urlpatterns = [
    path("user/auth/", obtain_auth_token, name="token-auth"),                   # Authentication
    path("user/register/", RegisterUserView.as_view(), name="register-user"),   # Registration
    path("user/", CurrentUserView.as_view(), name="current-user"),              # Retrieving user details
]