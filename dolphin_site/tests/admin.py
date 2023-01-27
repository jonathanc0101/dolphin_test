from django.contrib import admin

# Register your models here.
from .models import Delfin,Atributo,Atributo_Delfin

admin.site.register(Delfin)
admin.site.register(Atributo)
admin.site.register(Atributo_Delfin)
