from django.db import models
import datetime 

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion= models.TextField()
    imagen= models.ImageField(upload_to='blog/images')
    fecha= models.DateField(datetime.date.today)



