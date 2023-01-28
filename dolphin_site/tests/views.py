from django.shortcuts import render
from django.views import generic
import random
# Create your views here.

from .models import Delfin, Pregunta


def index(request):
    num_delfines = len(Delfin.objects.all())
    num_preguntas = len(Pregunta.objects.all())

    context = {"num_delfines": num_delfines, "num_preguntas": num_preguntas}

    return render(request, 'tests/index.html', context)


class DelfinDetailView(generic.DetailView):
    model = Delfin


def test(request):
    num_actual_preguntas = 20
    num_preguntas = len(Pregunta.objects.all())
    pregunta_list = list(Pregunta.objects.all())
    pregunta_list = random.sample(pregunta_list, num_actual_preguntas)

    context = {"num_preguntas": num_preguntas,
               "pregunta_list": pregunta_list, "num_actual_preguntas": num_actual_preguntas}

    return render(request, 'tests/test.html', context)
