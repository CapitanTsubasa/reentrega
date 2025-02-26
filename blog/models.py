from django.conf import settings
from django.db import models

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts_blog")

    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo