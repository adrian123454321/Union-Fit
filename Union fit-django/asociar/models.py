from django.db import models
class Asociar(models.Model):
	nombre= models.Charfield(max_length=50)
	correo= models.Charfield(max_length=50)
	direccion=models.Charfield(max_length=50)
	telefono=models.Charfield(max_length=20)
	precio=models.Charfield(max_length=20)

	def__str__(self):

		self.nombre
		self.correo
		self.direccion
		self.telefono
		self.precio
	

# Create your models here.
