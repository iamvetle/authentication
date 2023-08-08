from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.db import IntegrityError
from .models import CustomUser
from rest_framework import status


# Create your views here.

class CurrentUserView(APIView): # Function
    permission_classes = [IsAuthenticated] # Checks whether the the token is authenticated/valid

    def get(self, request): # Takes the token and returns the corresponding user information
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
# class 


# With IsAuthenticated permission, only requests with valid authentication tokens will be allowed to access this endpoint. If the token is missing or invalid, a 401 Unauthorized response will be returned.

class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            CustomUser.objects.create_user(
                email=data['email'], 
                first_name=data['first_name'], 
                last_name=data['last_name'], 
                phone=data['phone'], 
                password=data['password']
            )
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)