from django import forms
from .choices import RESPUESTA_CHOICES

class ResponderPreguntaForm(forms.Form):
    def __init__(self, pregunta_list,  *args, **kwargs):
        super(ResponderPreguntaForm, self).__init__(*args, **kwargs)

        for i, pregunta in enumerate(pregunta_list):
            self.fields[pregunta.id] = forms.ChoiceField(choices=RESPUESTA_CHOICES,initial=0, widget=forms.Select(), required=True,label=pregunta.texto)
