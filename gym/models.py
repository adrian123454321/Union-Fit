from django.db import models

# Create your models here.
from django.contrib.auth.models import user
class Perfil(models,Model);
usuario= models.OneToOneFild(user)
	telefono= models.Charfield(max_length=20)
	genero=models.Charfield(max_length=20)