from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from users.models import User
from users.serializer import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializer import UserListSerializer


class UserLoginAPIView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return Response({"tokens": response.data}, status=response.status_code)


class UserRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        birthday = data.get('birthday')

        # Проверка обязательных полей
        if not username or not password or not email or not birthday:
            return Response({"message": "Все поля обязательны для заполнения."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка уникальности username
        if User.objects.filter(username=username).exists():
            return Response({"message": "Пользователь с таким ником уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Создание пользователя
        User.objects.create_user(username=username, email=email, password=password, birthday=birthday)
        
        return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        print(request.headers)
        print(request.user)
        print(request.auth)
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)


class UserSignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            
            # Проверка прав доступа (например, только администраторы могут удалять других пользователей)
            if not request.user.is_staff and user != request.user:  # Убедитесь, что только администраторы могут удалять других пользователей
                return Response({"message": "У вас нет прав для удаления этого пользователя."}, status=status.HTTP_403_FORBIDDEN)

            user.delete()
            return Response({"message": "Пользователь успешно удалён."}, status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist:
            return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)


class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)

            # Проверка прав доступа (например, только администраторы могут обновлять других пользователей)
            if not request.user.is_staff and user != request.user:
                return Response({"message": "У вас нет прав для обновления этого пользователя."}, status=status.HTTP_403_FORBIDDEN)

            # Обновление полей пользователя
            for attr, value in request.data.items():
                setattr(user, attr, value)
            user.save()

            return Response({"message": "Пользователь успешно обновлён."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

# class ProfileTemplateView(LoginRequiredMixin, TemplateView):
#     template_name = "users/profile.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["user"] = self.request.user
#         return context


# class ProfileDetailView(DetailView):
#     template_name = "users/profile.html"
#     queryset = users.models.User.objects.all()


# class UserDeleteView(LoginRequiredMixin, RedirectView):
#     url = reverse_lazy("homepage:main")

#     def get(self, request, *args, **kwargs):
#         request.user.delete()
#         return super().get(request, *args, **kwargs)


# class UserListView(ListView):
#     queryset = users.models.User.objects.all()