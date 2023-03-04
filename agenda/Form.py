from django import forms

from agenda.models import Agenda

class Formulario(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
