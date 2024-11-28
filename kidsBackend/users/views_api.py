from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny  # Разрешить доступ без аутентификации
from django.contrib.auth import authenticate
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Login API
class UserLoginAPIView(jwt_views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
                response = super().post(request, *args, **kwargs)


# Logout API
class UserLogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Здесь можно добавить логику для выхода пользователя
        return Response({"message": "Logout successful"})

# Register API
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Убираем требование авторизации для регистрации

# User List and Create API
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Detail, Update, and Delete API
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Current User Profile API
class UserProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Profile Edit API
class UserProfileEditAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile Delete API
class UserProfileDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        request.user.delete()
        return Response({"message": "Profile deleted"}, status=status.HTTP_204_NO_CONTENT)