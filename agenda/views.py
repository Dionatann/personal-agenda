from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import agenda
from agenda.Form import Formulario
from agenda.models import Agenda


# Criando as views
def home(request):
    compromissos = Agenda.objects.all()
    form = Formulario()
    return render(request, "home.html", {"compromissos": compromissos, 'form': form})


#Adicona compromissos
def incluirCompromisso(request):
    data = request.POST['dataC']
    try:
        Agenda.objects.get(data=data, horaDeInicio=request.POST['horaInicio'])
        messages.error(request, "Não foi possível realizar")
        return HttpResponseRedirect(reverse("home"))
    except ObjectDoesNotExist:
        agenda = Agenda(data=request.POST['dataC'], horaDeInicio=request.POST['horaInicio'],
                        horaDeTermino=request.POST['horaTermino'], descricao=request.POST['descricao'],
                        duracao=request.POST['duracao'])
        agenda.save()
        return HttpResponseRedirect(reverse("home"))


# excluir compromisso
def excluirCompromisso(request):
    id = request.POST['id']
    c = Agenda.objects.get(id=id)
    c.delete()
    return JsonResponse({'Deletado': 'sim'})


# editar compromisso
def editarCompromisso(request, id):
    agenda = Agenda.objects.get(id=id)
    form = Formulario(instance=Agenda)
    return render(request, "editar.html", {"form": form, 'agendaDados': agenda})


# salva dados editados
def salvaDadosEditado(request, id):
    compromisso = Agenda.objects.get(id=id)
    compromisso.data = request.POST['data']
    compromisso.horaDeInicio = request.POST['horaInicio']
    compromisso.horaDeTermino = request.POST['horaTermino']
    compromisso.descricao = request.POST['descricao']
    compromisso.duracao = request.POST['duracao']
    compromisso.save()
    messages.success(request, "Editado com sucesso!")
    return HttpResponseRedirect(reverse('home'))


# consulta Por Data
def consultaPorData(request):
    data = request.POST['data']
    consulta = Agenda.objects.filter(data=data)
    return render(request, "consultaPorData.html", {'consulta': consulta})

