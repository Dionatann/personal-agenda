from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect

from agenda.Form import Formulario
from agenda.models import Agenda


class CompromissosForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'


# Criando as views
def home(request):
    compromissos = Agenda.objects.all()
    form = CompromissosForm()
    return render(request, "home.html", {"compromissos": compromissos, 'form': CompromissosForm})


def incluirCompromisso(request):
    try:
        Agenda.objects.get(data=request.POST['data'], horaDeInicio=request.POST['horaInicio'])
        return JsonResponse({"Erro": "Já existe um compromisso para este horário!"}, safe=False)
    except ObjectDoesNotExist:
        agenda = Agenda(data=request.POST['data'], horaDeInicio=request.POST['horaInicio'],
                        horaDeTermino=request.POST['horaTermino'], descrição='dgdsklgkl',
                        duração=request.POST['horaTermino'] - request.POST['horaInicio'])
        agenda.save()
        return JsonResponse({"Sucesso": "Cadastrado com Sucesso!"}, safe=False)


def excluirCompromisso(request):
    return JsonResponse()


def ConsultaCompromisso(request):
    return JsonResponse()
