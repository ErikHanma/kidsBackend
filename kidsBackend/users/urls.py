from django.contrib.auth import views
from django.contrib.auth.forms import (
    AuthenticationForm
)

from django.urls import path, reverse_lazy

import users.forms
import users.views

__all__ = []


app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(
            template_name="users/login.html",
            authentication_form=users.forms.custom_auth_form(
                AuthenticationForm,
            ),
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(
            template_name="users/logout.html",
        ),
        name="logout",
    ),
    path(
        "register/",
        users.views.SignupFormView.as_view(),
        name="signup",
    ),
    path(
        "user_list/",
        users.views.UserListView.as_view(),
        name="user_list",
    ),
    path(
        "<int:pk>/",
        users.views.ProfileDetailView.as_view(),
        name="user_detail",
    ),
    path(
        "profile/",
        users.views.ProfileTemplateView.as_view(),
        name="profile",
    ),
    path(
        "profile/edit/",
        users.views.ProfileEditFormView.as_view(),
        name="profile_edit",
    ),
    path(
        "profile/delete/",
        users.views.UserDeleteView.as_view(),
        name="profile_delete",
    ),
]
