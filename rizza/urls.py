"""
URL configuration for rizza project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pizzas/", include("pizza.urls")),
]
