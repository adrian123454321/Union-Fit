from django.db import models
class Asociar(models.Model):
 	nombre = models.CharField(max_length=50)
 	correo = models.CharField(max_length=50)
 	direccion = models.CharField(max_length=50)
 	telefono = models.CharField(max_length=20)
 	precio = models.CharField(max_length=20)
 
 	def __str__(self):
 		return " %s - %s - %s - %s - %s "%(
 		self.nombre,
 		self.correo,
 		self.direccion,
 		self.telefono,
 		self.precio)
 


# Create your models here.
