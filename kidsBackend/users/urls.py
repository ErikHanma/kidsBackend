from django.urls import path
from users.views import UserDeleteAPIView, UserUpdateAPIView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import (
    UserLoginAPIView,
    UserSignupAPIView,
    UserRegisterAPIView,
    UserProfileAPIView,
    UserListView
)

app_name = "users"

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='signup'),
    # path('register/', UserSignupAPIView.as_view(), name='signup'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/delete/<int:user_id>/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('users/update/<int:user_id>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/', UserListView.as_view(), name='user-list'),
    # path('user_list/', UserListCreateAPIView.as_view(), name='user_list'),
    # path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_detail'),
    # path('profile/edit/', UserProfileEditAPIView.as_view(), name='profile_edit'),
    # path('profile/delete/', UserProfileDeleteAPIView.as_view(), name='profile_delete'),
]