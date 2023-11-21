from django.db import models
from django.db.models.fields import CharField ,URLField
from django.db.models.fields.files import ImageField

#Charfield es importar caracteres


class Project(models.Model):
    titulo =  CharField(max_length=100)
    descripcion = CharField(max_length=300)
    imagen = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
    
    