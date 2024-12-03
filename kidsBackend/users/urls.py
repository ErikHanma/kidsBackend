from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import (
    UserLoginAPIView,
    UserRegisterAPIView,
    UserProfileAPIView,
    UserDetailUpdateDeleteAPIView,
    UserListView,
    UserListView,
    UserDeleteAPIView,
    # UserUpdateAPIView
)

app_name = "users"

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='signup'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('users/delete/<int:user_id>/', UserDetailUpdateDeleteAPIView.as_view(), name='user-delete'),
    path('users/update/<int:user_id>/', UserDetailUpdateDeleteAPIView.as_view(), name='user-update'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/delete/<int:user_id>/', UserDeleteAPIView.as_view(), name='user-delete'),
    # path('users/update/<int:user_id>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailUpdateDeleteAPIView.as_view(), name='user_detail'),
]