from django.conf import settings
import django.conf.urls.static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "auth/", include(("users.urls")), name="users",
    ),
    path(
        "",
        include(
            "homepage.urls",
        ),
        name="homepage",
    ),

]
