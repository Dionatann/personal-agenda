from agenda import views as agenda
from django.urls import path


urlpatterns = [
    path('', agenda.home, name="home"),
    path('salvar', agenda.incluirCompromisso, name="salvar_compromisso"),
    path('excluir', agenda.excluirCompromisso, name="excluir"),
    path('editar', agenda.incluirCompromisso, name="editar"),

]
