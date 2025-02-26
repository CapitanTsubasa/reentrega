from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username

class Avatar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts_main")
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()