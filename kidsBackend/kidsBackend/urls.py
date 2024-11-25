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

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
    if settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
