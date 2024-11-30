from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import APIView
import rest_framework.generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializer import UserListSerializer
from django.contrib.auth import get_user_model

from users.models import User
from users.serializer import UserSerializer, RegisterSerializer


class UserLoginAPIView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return Response({"tokens": response.data}, status=response.status_code)


class UserRegisterAPIView(rest_framework.generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    # def post(self, request):
    #     data = request.data
    #     username = data.get('username')
    #     password = data.get('password')
    #     email = data.get('email')
    #     birthday = data.get('birthday')

    #     # Проверка обязательных полей
    #     if not username or not password or not email or not birthday:
    #         return Response({"message": "Все поля обязательны для заполнения."}, status=status.HTTP_400_BAD_REQUEST)

    #     # Проверка уникальности username
    #     if User.objects.filter(username=username).exists():
    #         return Response({"message": "Пользователь с таким ником уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        
    #     # Создание пользователя
    #     User.objects.create_user(username=username, email=email, password=password, birthday=birthday)
        
    #     return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)


class UserListAPIView(rest_framework.generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailUpdateDeleteAPIView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    