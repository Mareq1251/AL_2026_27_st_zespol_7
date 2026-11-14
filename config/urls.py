from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from katalog.views import lista_zasobow

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("zasoby/", lista_zasobow, name="lista_zasobow"),
]