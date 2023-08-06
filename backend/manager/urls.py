from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CurrentUserView

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"), # The built in login view that DRF provides | axios.post to here
    path("api/users/me/", CurrentUserView.as_view(), name="current-user")
]