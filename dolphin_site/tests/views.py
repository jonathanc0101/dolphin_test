from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Delfin,Pregunta

def index(request):
    num_delfines = len(Delfin.objects.all())
    num_preguntas = len(Pregunta.objects.all())

    context = {"num_delfines":num_delfines,"num_preguntas":num_preguntas}
    
    return render(request, 'tests/index.html',context)

class PreguntaListView(generic.ListView):
    model = Pregunta

class DelfinDetailView(generic.DetailView):
    model = Delfin