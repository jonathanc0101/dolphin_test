from django.db import models

# Create your models here.

class Delfin(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')


class Atributo(models.Model):
    """para no hardcodear los atributos"""
    descripcion = models.CharField(max_length=100)

class Atributo_Delfin(models.Model):
    """un delfin tiene muchos atributos"""
    delfin = models.ForeignKey(Delfin, on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)