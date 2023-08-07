from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views import View


# Create your views here.

class CurrentUserView(APIView): # Function
    permission_classes = [IsAuthenticated] # Checks whether the the token is authenticated/valid

    def get(self, request): # Takes the token and returns the corresponding user information
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
# class 


# With IsAuthenticated permission, only requests with valid authentication tokens will be allowed to access this endpoint. If the token is missing or invalid, a 401 Unauthorized response will be returned.


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
from .models import CustomUser

@csrf_exempt
def RegisterUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            CustomUser.objects.create_user(
                email=data['email'], 
                first_name=data['first_name'], 
                last_name=data['last_name'], 
                phone=data['phone'], 
                password=data['password']
            )
            return JsonResponse({"message": "User created successfully."}, status=201)
        except IntegrityError:
            return JsonResponse({"error": "A user with this email already exists."}, status=400)