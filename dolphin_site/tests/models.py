from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Delfin(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)


    def __str__(self):
        return "{nombre}: {descripcion}".format(nombre = self.nombre,descripcion=self.descripcion)


class Atributo(models.Model):
    """para no hardcodear los atributos"""
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
    

class Atributo_Delfin(models.Model):
    """un delfin tiene muchos atributos"""
    delfin = models.ForeignKey(Delfin, on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0,validators=[MinValueValidator(-2),MaxValueValidator(2)])