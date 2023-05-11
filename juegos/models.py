from django.db import models

# Create your models here.

class Juegos(models.Model):
    nombreJ = models.CharField(max_length=200)
    ano = models.DateField()
    imagen =models.ImageField(upload_to='juegos/images/')
    
    def __str__(self):
        return self.nombreJ