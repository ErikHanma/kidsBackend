import re

from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', "birthday"]

    def validate_password(self, value):
        """
        Проверка, что пароль содержит хотя бы одну заглавную букву, строчную букву, цифру и специальный символ.
        """
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов.")
        
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну строчную букву.")
        
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну заглавную букву.")
        
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        
        if not re.search(r"[@#$%^&*]", value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы один специальный символ (@#$%^&*).")
        
        return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid username or password')
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']