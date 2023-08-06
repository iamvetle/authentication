from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CurrentUserView

urlpatterns = [
    path("user/auth/", obtain_auth_token, name="token-auth"), # The built in login view that DRF provides | axios.post to here
    path("user/", CurrentUserView.as_view(), name="current-user")
    # LATER path("user/register") as in POST new user
    # MAYBE path("user/logout")
]