from django.shortcuts import render
from django.views import generic
import random

# Create your views here.

from .models import Delfin, Pregunta, Ubicador, Atributo
from .forms.forms import ResponderPreguntaForm
from django.shortcuts import redirect

def index(request):
    num_delfines = len(Delfin.objects.all())
    num_preguntas = len(Pregunta.objects.all())

    context = {"num_delfines": num_delfines, "num_preguntas": num_preguntas}

    return render(request, 'tests/index.html', context)


class DelfinDetailView(generic.DetailView):
    model = Delfin


def test(request):

    atributos = list(Atributo.objects.all())

    preguntas_por_atributo = 3
    cant_atributos = len(atributos)
    num_actual_preguntas = preguntas_por_atributo * cant_atributos

    pregunta_list = Pregunta.objects.all()
    pregunta_list_real = []
    num_preguntas = len(pregunta_list)


    for atributo in atributos:
        pregunta_list_real.extend(random.sample(list(Pregunta.objects.filter(atributo=atributo)), preguntas_por_atributo))


    context = {}
    context["num_preguntas"] = num_preguntas
    context["pregunta_list"] = pregunta_list_real
    context["num_actual_preguntas"] = num_actual_preguntas
    context["form"] = ResponderPreguntaForm(pregunta_list_real)

    return render(request, 'tests/test.html', context)

def responder(request):
    if request.method=='POST':

        respuesta_procesada = dict(request.POST)
        respuesta_procesada.pop("csrfmiddlewaretoken",None)

        for item,val in respuesta_procesada.items():
            respuesta_procesada[item] = int(val[0])

        if(len(respuesta_procesada)>0): ##es valido
            id_delfin = Ubicador.ubicar_respuestas(respuesta_procesada).pk
            return redirect('delfin-detail', pk=id_delfin)
    
    