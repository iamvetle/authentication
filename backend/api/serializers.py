# Handles user registration
# Kind of like a form

from .models import CustomUser  # Built-in django model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser

        fields = ['password', 'first_name', 'last_name', 'email', 'phone'] #TODO expand this later
        extra_kwargs = {'password': {'write_only': True}} # prevents sending hashed passwords back to web clientc