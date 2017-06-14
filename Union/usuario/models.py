from django.db import models
class Usuario(models.Model):
	nombre= models.CharField(max_length=20)
	correo= models.CharField(max_length=30)
	
	def __str__(self):
		return"%s - %s"%(
			self.nombre,
			self.correo)
# Create your models here.
