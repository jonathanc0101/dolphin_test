from django.contrib import admin

# Register your models here.
from .models import Delfin, Atributo, Atributo_Delfin, Pregunta


class AtributoDelfinInline(admin.TabularInline):
    model = Atributo_Delfin
    extra = 0


class DelfinAdmin(admin.ModelAdmin):
    fieldsets = [("Nombre", {"fields": ["nombre"]}),
                 ("Descripcion", {"fields": ["descripcion"]})]
    inlines = [AtributoDelfinInline]

admin.site.register(Delfin,DelfinAdmin)
admin.site.register(Atributo)
admin.site.register(Atributo_Delfin)
admin.site.register(Pregunta)
