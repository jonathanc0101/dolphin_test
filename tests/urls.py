
from django.urls import path

from .views import index,test,DelfinDetailView,responder

urlpatterns = [
    path('', index, name='index'),
    path('test', test, name='test'),
    path('delfin/<int:pk>', DelfinDetailView.as_view(), name='delfin-detail'),
    path('responder', responder, name='responder'),
]