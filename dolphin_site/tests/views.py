from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Delfin,Pregunta

def index(request):
    num_delfines = len(Delfin.objects.all())
    context = {"num_delfines":num_delfines}
    return render(request, 'index.html',context)

def test(request):
    num_preguntas=len(Pregunta.objects.all())
    context = {"num_preguntas":num_preguntas}
    return render(request, 'test.html',context)