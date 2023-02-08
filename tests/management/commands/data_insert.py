
from ...models import Delfin, Pregunta, Atributo, Atributo_Delfin
from django.core.management.base import BaseCommand, CommandError

data_total = ["""Apertura a la experiencia


Tengo excelentes ideas
Entiendo rápido las cosas
Uso palabras difíciles
Estoy lleno de ideas

No me interesan las abstracciones
No tengo buena imaginación
Tengo dificultades para entender ideas abstractas""",
              """Extraversión


Soy el alma de la fiesta
No me importa ser el centro de atención
Me siento cómodo con la gente
Comienzo conversaciones
Hablo con muchas personas diferentes en las fiestas

No hablo mucho
Pienso mucho antes de hablar o actuar
No me gusta llamar la atención sobre mí mismo
Estoy callado con extraños
No tengo intención de hablar en grandes multitudes""",
              """Conciencia/Escrupulosidad


Siempre estoy preparado
Presto atención a los detalles
Tengo tareas hechas de inmediato
Me gusta el orden
Sigo un horario
Soy exigente en mi trabajo
Nunca olvido mis pertenencias
Siempre termino siendo útil para la mayoría de las cosas
A menudo recuerdo dónde puse mis cosas por última vez
Presto atención a mis deberes""",
              """Cordialidad / Amabilidad / Afabilidad


Estoy interesado en las personas
Simpatizo con los sentimientos de los demás
Tengo un corazón suave
Tomo tiempo para los demás
Siento las emociones de los demás
Hago que la gente se sienta a gusto

No estoy muy interesado en los demás
Insulto a la gente
No estoy interesado en los problemas de otras personas
Siento poca preocupación por los demás""",
              """Neuroticismo


Me irrito fácilmente
Me estreso fácilmente
Me enfado con facilidad
Tengo cambios de humor frecuentes
Me preocupan las cosas
Estoy mucho más ansioso que la mayoría de las personas

Estoy relajado la mayor parte del tiempo
Rara vez me siento triste"""]

delfines = [
    {
        "nombre":       "Pakicetus",
        "descripcion":  "El es Pakicetus, no es un delfín sinó que es el ancestro mas antigüo que conocemos, es reservado y no tiene ganas de arriesgarse, pero le importa mucho la familia.",
        "foto_url":     "https://i.redd.it/wp5froy0dt331.jpg",
        "atributos": {
            "Apertura a la experiencia": -4,
            "Extraversión": -2,
            "Conciencia/Escrupulosidad": 5,
            "Cordialidad / Amabilidad / Afabilidad": 5,
            "Neuroticismo": -3
        }
    },
    {
        "nombre":       "María",
        "descripcion":  "María vivió toda la vida exigiendose al límite, y por lo tanto siempre está cansada, le gusta comer almejas porque abrirlas supone un pequeño desafío, es adicta a la adrenalina y si pudiese, le gustaría saltar en paracaídas.",
        "foto_url":     "https://2.bp.blogspot.com/-Eif3f2DimF8/UZr1fX9Wt-I/AAAAAAAAALI/bKOFopUJd3M/s1600/sad+dolphin.jpg",
        "atributos": {
            "Apertura a la experiencia": 6,
            "Extraversión": 4,
            "Conciencia/Escrupulosidad": -2,
            "Cordialidad / Amabilidad / Afabilidad": -3,
            "Neuroticismo": 4
        }
    },
    {
        "nombre":       "Juanjo Soto",
        "descripcion":  "Juanjo es un deportista nato, usar su cuerpo le divierte mucho, le encanta aprender cosas nuevas y aplicarlas en distintos problemas.",
        "foto_url":     "https://www.sunnyskyz.com/images/webpics/b9dtp-happy-jumping-dolphin.jpg",
        "atributos": {
            "Apertura a la experiencia": 5,
            "Extraversión": 3,
            "Conciencia/Escrupulosidad": 2,
            "Cordialidad / Amabilidad / Afabilidad": 0,
            "Neuroticismo": -3
        }
    },
    {
        "nombre":       "Alejandra",
        "descripcion":  "La naturaleza la convirtió en una máquina perfecta de matar.",
        "foto_url":     "https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2016/03/orca.jpg?w=1560&ssl=1",
        "atributos": {
            "Apertura a la experiencia": 6,
            "Extraversión": 6,
            "Conciencia/Escrupulosidad": 6,
            "Cordialidad / Amabilidad / Afabilidad": 4,
            "Neuroticismo": -6
        }
    },
    {
        "nombre":       "Uriel",
        "descripcion":  "Uriel nunca encajó, de hecho ni siquiera es un delfín, pero decidimos darle un lugar porque es buena persona y no le hace mal a nadie. Le gustan las caminatas por la playa y las excursiones, es reservado con si mismo pero aún así se preocupa mucho por la gente.",
        "foto_url":     "https://dondevive.net/wp-content/uploads/2018/01/manati.jpg",
        "atributos": {
            "Apertura a la experiencia": 1,
            "Extraversión": -3,
            "Conciencia/Escrupulosidad": 5,
            "Cordialidad / Amabilidad / Afabilidad": 5,
            "Neuroticismo": -5
        }
    },
    {
        "nombre":       "Ernie",
        "descripcion":  "Es una marsopa, altamente sociable, le gusta hacer chistes para entretener a los demás, dice que alegrarle el dia a otros le alegra su propio día.",
        "foto_url":     "https://imgs.search.brave.com/CDWakgF2B7B71SSdiJ5T8qwtTF1YQUGYff5WHDibNFk/rs:fit:766:225:1/g:ce/aHR0cHM6Ly90c2Uy/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5k/OFp4OXBlNXpod243/aDc3cmxOU1pnQUFB/QSZwaWQ9QXBp",
        "atributos": {
            "Apertura a la experiencia": 5,
            "Extraversión": 5,
            "Conciencia/Escrupulosidad": -3,
            "Cordialidad / Amabilidad / Afabilidad": 6,
            "Neuroticismo": 3
        }
    },
    {
        "nombre":       "Constantopoulos",
        "descripcion":  "Le gusta matar por diversión, se enoja facilmente, es mandón, rezonga por todo y le cuesta dormir porque sus problemas lo agobian hasta altas horas de la noche. Debería ir al psicologo para evitar que los otros delfines con los que interactúa necesiten de uno.",
        "foto_url":     "https://i2-prod.mirror.co.uk/incoming/article1265646.ece/ALTERNATES/s1227b/Laughing-Dolphin-1.jpg",
        "atributos": {
            "Apertura a la experiencia": 2,
            "Extraversión": 2,
            "Conciencia/Escrupulosidad": -3,
            "Cordialidad / Amabilidad / Afabilidad": -4,
            "Neuroticismo": 5
        }
    }
]

# https://es.wikipedia.org/wiki/Modelo_de_los_cinco_grandes#Consenso_de_los_Cinco_Grandes

def generar_delfines(delfines):
    for delfin in delfines:
        generar_delfin(delfin["nombre"], descripcion=delfin["descripcion"], foto_url=delfin["foto_url"], atributos=delfin["atributos"])

def generar_delfin(nombre, descripcion, foto_url, atributos):
    delfin = Delfin.objects.create(
        nombre=nombre, descripcion=descripcion, foto_url=foto_url)

    for atributo, valor in atributos.items():
        atributo_encontrado = Atributo.objects.filter(descripcion=atributo).first()

        if(atributo_encontrado is not None):
            Atributo_Delfin.objects.create(
                delfin=delfin, atributo_id=atributo_encontrado.pk, valor=valor)


def generar_pregunta(atrib_id, texto, positivo):
    Pregunta.objects.create(atributo_id=atrib_id,
                            texto=texto, positivo=positivo)


def generar_preguntas(atrib_id, preguntas, positivo):
    for texto in preguntas:
        generar_pregunta(atrib_id, texto, positivo)


def generar_atributo(descripcion) -> id:
    atrib = Atributo.objects.create(descripcion=descripcion)
    return atrib.pk


def separar_datos(data):
    data_1st_pass = data.split("\n\n\n")
    atributo = data_1st_pass.pop(0)

    data_2nd_pass = data_1st_pass[0].split("\n\n")
    positivos = data_2nd_pass.pop(0)
    positivos = positivos.split("\n")

    if (len(data_2nd_pass) > 0):
        negativos = data_2nd_pass.pop(0)
        negativos = negativos.split("\n")

        return (atributo, positivos, negativos)
    else:
        return (atributo, positivos)


def generar_data(data):
    datos_procesados = [separar_datos(dato) for dato in data]

    for dato_procesado in datos_procesados:
        # generamos atributo
        id = generar_atributo(dato_procesado[0])

        # generamos preguntas positivas
        generar_preguntas(id, dato_procesado[1], True)

        if (len(dato_procesado) > 2):
            # generamos preguntas negativas si hay
            generar_preguntas(id, dato_procesado[2], False)

    generar_delfines(delfines)


def generar_data_bd():
    generar_data(data_total)


class Command(BaseCommand):
    help = 'Generates the database for the use of the app'

    def handle(self, *args, **options):
        generar_data_bd()
