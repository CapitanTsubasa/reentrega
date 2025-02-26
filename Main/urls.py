from django.urls import path
from .views import register, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.shortcuts import render
from Main.views import login_view, perfil


app_name = "Main"

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),
    path("about/", views.about, name="about"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register_view, name="register"),
    path("usuarios/", views.listar_usuarios, name="listar_usuarios"),
    path("base/", views.base_view, name="base"),
]

# Configurar media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
