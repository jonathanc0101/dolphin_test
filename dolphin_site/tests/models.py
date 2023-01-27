from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from math import sqrt

class Ubicador():
    """se encarga de obtener la menor distancia a todos los delfines y nos dice cual somos"""
    def ubicar(atributos):
        """recibe un diccionario con los atributos"""
        delfines = Delfin.objects.all()
        distancias_a_delfines = {}

        for delfin in delfines:
            atributos_delfin = delfin.get_atributos()
            distancias_a_delfines[delfin.id] = 0

            suma_cuadrados = 0

            for atributo in atributos_delfin:

                if(atributos[atributo.atributo]): #si el usuario nos dio el atributo entonces lo tenemos en cuenta
                    suma_cuadrados += (atributo.valor - atributos[atributo.atributo])**2
            
            distancias_a_delfines[delfin.id] = sqrt(suma_cuadrados)
        
        min_value = min(distancias_a_delfines.values())

        #retornamos el primero de los menores valores encontrados (en caso de que se repitan)
        result = [key for key, value in distancias_a_delfines.iteritems() if value == min_value][0]

        

class Delfin(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    
    def get_atributos(self):
        return list(Atributo_Delfin.objects.filter(delfin=self))

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

    def __str__(self):
        return "{atributo}: {valor}".format(atributo = self.atributo, valor = self.valor)