from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Ubicador

def index(request):
    delfin_ubicado = Ubicador.ubicar({"Tranquilidad":0,"Calma":-2,"Irritabilidad":-1,"Amabilidad":-1})
    atributos_delfin = [str(x) for x in delfin_ubicado.get_atributos()]
    return HttpResponse(str([str(delfin_ubicado),atributos_delfin]))#test