from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import APIView
import rest_framework.generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializer import UserListSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializer import UserSerializer, RegisterSerializer
import logging


class UserLoginAPIView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return Response({"tokens": response.data}, status=response.status_code)


class UserRegisterAPIView(rest_framework.generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)


# class UserListAPIView(rest_framework.generics.ListAPIView):
class UserSignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(APIView):
    """
    Получение списка всех пользователей.
    """
    def get(self, request):
        users = User.objects.all()
        users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
        return Response(users_data, status=status.HTTP_200_OK)



class UserDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    