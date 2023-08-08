# Handles user registration (kind of like a form)

from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = ['password', 'first_name', 'last_name', 'email', 'phone']
        extra_kwargs = {'password': {'write_only': True}} # Prevents sending hashed passwords back to client