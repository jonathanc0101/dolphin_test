
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('delfin/<int:pk>', views.DelfinDetailView.as_view(), name='delfin-detail'),
]