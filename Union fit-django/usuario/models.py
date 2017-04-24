from django.db import models
class Usuario(object):
	nombre= models.Charfield(max_length=20)
	correo= models.Charfield(max_length=30)
	edad=models.Charfield(max_length=2)
	telefono=models.Charfield(max_length=20)
	contraseña=models.Charfield(max_length=20)
	usuario=models.Charfield(max_length=15)

	def__str__(self):
		self.nombre
		self.correo
		self.edad
		self.telefono
		self.contraseña
		self.usuario
# Create your models here.
