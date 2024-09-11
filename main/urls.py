"""Description"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("oauth/", include("company.urls")),
    path("social-auth/", include("social_django.urls", namespace="social")),
]
