from django.db import models


class Tarea(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'