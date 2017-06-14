from django.db import models
class Administrador(models.Model):
 	nombre = models.CharField(max_length=50)
 	correo = models.CharField(max_length=50)
 	telefono = models.CharField(max_length=20)
 	usuarios = models.CharField(max_length=20)
 
 	def __str__(self):
 		return " %s - %s - %s - %s  "%(
 		self.nombre,
 		self.correo,
 		self.telefono,
 		self.usuarios,)
 
# Create your models here.
