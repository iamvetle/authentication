# Handles user registration
# Kind of like a form

from django.contrib.auth.models import User # Built-in django model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['username', 'password', 'first_name', 'last_name', 'email'] #TODO expand this later
        extra_kwargs = {'password': {'write_only': True}} # prevents sending hashed passwords back to web client