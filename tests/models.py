from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from math import sqrt

class Ubicador():
    """se encarga de obtener la menor distancia a todos los delfines y nos dice cual somos"""


    def ubicar_respuestas(ids_valores_respuestas_dict):
        """recibe un diccionario {id:valor} de cada una de las respuestas"""
        atributos = {}

        for id,valor in ids_valores_respuestas_dict.items():
            # obtenemos el atributo
            pregunta = Pregunta.objects.get(pk=id)
            atrib = pregunta.atributo

            if(atrib.descripcion not in atributos):
                atributos[atrib.descripcion] = 0   
            
            atributos[atrib.descripcion] += valor
            

        return Ubicador.ubicar(atributos)

    def ubicar(atributos):
        """recibe un diccionario con los atributos, retorna el delfin mas cercano"""
        delfines = list(Delfin.objects.all())
        distancias_a_delfines = {}


        for delfin in delfines:
            atributos_delfin = delfin.get_atributos()
            distancias_a_delfines[delfin.id] = 0

            suma_cuadrados = 0

            for atributo in atributos_delfin:

                atributo_actual = str(atributo.atributo)
                
                if(atributo_actual in atributos): #si el usuario nos dio el atributo entonces lo tenemos en cuenta
                    suma_cuadrados += (atributo.valor - atributos[atributo_actual])**2
                
            distancias_a_delfines[delfin.id] = sqrt(suma_cuadrados)
        
        min_value = min(distancias_a_delfines.values())

        #retornamos el primero de los menores valores encontrados (en caso de que se repitan)
        result_id = [key for key, value in distancias_a_delfines.items() if value == min_value][0]
        return Delfin.objects.get(pk=result_id)
        

class Delfin(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    foto_url = models.CharField(max_length=400)
    
    def get_atributos(self):
        return list(Atributo_Delfin.objects.filter(delfin=self))

    def __str__(self):
        return "{nombre}: {descripcion}".format(nombre = self.nombre,descripcion=self.descripcion)

    class Meta:
        verbose_name = "delfin"
        verbose_name_plural = "delfines"

class Atributo(models.Model):
    """para no hardcodear los atributos"""
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
    

class Atributo_Delfin(models.Model):
    """un delfin tiene muchos atributos"""
    delfin = models.ForeignKey(Delfin, on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0,validators=[MinValueValidator(-10),MaxValueValidator(10)])

    def __str__(self):
        return "{atributo}: {valor}".format(atributo = self.atributo, valor = self.valor)

    class Meta:
        verbose_name = "atributo de delfin"
        verbose_name_plural = "atributo de delfines"
        ordering = ['atributo']


class Pregunta(models.Model):
    """una pregunta afecta a un atributo en especifico"""
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    positivo = models.BooleanField(default=True)

    def __str__(self):
        positivo_mostrar = "positivo"
        if(not self.positivo):
            positivo_mostrar = "negativo"

        return "{atributo}/{positivo}: {texto}".format(atributo = self.atributo, positivo = positivo_mostrar, texto = self.texto)
