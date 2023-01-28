
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preguntas', views.PreguntaListView.as_view(), name='preguntas'),
]