
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preguntas', views.PreguntaListView.as_view(), name='preguntas'),
    path('delfin/<int:pk>', views.DelfinDetailView.as_view(), name='delfin-detail'),
]