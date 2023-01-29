
from .models import Delfin,Pregunta,Atributo

data_total = ["""Apertura a la experiencia


Tengo excelentes ideas
Entiendo rápido las cosas
Uso palabras difíciles
Estoy lleno de ideas

No me interesan las abstracciones
No tengo buena imaginación
Tengo dificultades para entender ideas abstractas"""
,"""Extraversión


Soy el alma de la fiesta
No me importa ser el centro de atención
Me siento cómodo con la gente
Comienzo conversaciones
Hablo con muchas personas diferentes en las fiestas

No hablo mucho
Pienso mucho antes de hablar o actuar
No me gusta llamar la atención sobre mí mismo
Estoy callado con extraños
No tengo intención de hablar en grandes multitudes"""
,"""Conciencia/Escrupulosidad


Siempre estoy preparado
Presto atención a los detalles
Tengo tareas hechas de inmediato
Me gusta el orden
Sigo un horario
Soy exigente en mi trabajo
Nunca olvido mis pertenencias
Siempre termino siendo útil para la mayoría de las cosas
A menudo recuerdo dónde puse mis cosas por última vez
Presto atención a mis deberes"""
,"""Cordialidad / Amabilidad / Afabilidad


Estoy interesado en las personas
Simpatizo con los sentimientos de los demás
Tengo un corazón suave
Tomo tiempo para los demás
Siento las emociones de los demás
Hago que la gente se sienta a gusto

No estoy muy interesado en los demás
Insulto a la gente
No estoy interesado en los problemas de otras personas
Siento poca preocupación por los demás"""
,"""Neuroticismo


Me irrito fácilmente
Me estreso fácilmente
Me enfado con facilidad
Tengo cambios de humor frecuentes
Me preocupan las cosas
Estoy mucho más ansioso que la mayoría de las personas

Estoy relajado la mayor parte del tiempo
Rara vez me siento triste"""]

## https://es.wikipedia.org/wiki/Modelo_de_los_cinco_grandes#Consenso_de_los_Cinco_Grandes

def generar_pregunta(atrib_id,texto,positivo):
    Pregunta.objects.create(atributo_id = atrib_id,texto = texto,positivo = positivo)

def generar_preguntas(atrib_id,preguntas,positivo):
    for texto in preguntas:
        generar_pregunta(atrib_id,texto,positivo)


def generar_atributo(descripcion) -> id:
    atrib = Atributo.objects.create(descripcion=descripcion)
    return atrib.pk

def separar_datos(data):
    data_1st_pass = data.split("\n\n\n")
    atributo = data_1st_pass.pop(0)

    data_2nd_pass = data_1st_pass[0].split("\n\n")
    positivos = data_2nd_pass.pop(0)
    positivos = positivos.split("\n")

    if(len(data_2nd_pass) > 0):
        negativos = data_2nd_pass.pop(0)
        negativos = negativos.split("\n")

        return (atributo,positivos,negativos)
    else:
        return (atributo,positivos)
        

def generar_data(data):
    datos_procesados = [separar_datos(dato) for dato in data]

    for dato_procesado in datos_procesados:
        #generamos atributo
        id = generar_atributo(dato_procesado[0])
        
        #generamos preguntas positivas
        generar_preguntas(id,dato_procesado[1],True)
        
        if(len(dato_procesado) > 2):
            #generamos preguntas negativas si hay
            generar_preguntas(id,dato_procesado[2],False)
    

def generar_data_bd():
    generar_data(data_total)

