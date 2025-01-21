from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

app_name = "Main"

urlpatterns = [
    path("", views.index, name="index"),
    path("perfil/", views.perfil, name="perfil"),
    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),
    path("about/", views.about, name="about"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)