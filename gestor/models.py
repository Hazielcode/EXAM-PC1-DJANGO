from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.titulo
