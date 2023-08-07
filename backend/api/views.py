from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated] # Checks whether the the token is authenticated/valid

    def get(self, request): # Takes the token and returns the corresponding user information
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
# class 


# With IsAuthenticated permission, only requests with valid authentication tokens will be allowed to access this endpoint. If the token is missing or invalid, a 401 Unauthorized response will be returned.