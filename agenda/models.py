from django.db import models


# Criando objeto Agenda
class Agenda(models.Model):
    data = models.DateField()
    horaDeInicio = models.TimeField(verbose_name="hora de início")
    descricao = models.CharField(max_length=100, null=False, blank=False)
    duracao = models.CharField(max_length=150, null=False, blank=False)
    horaDeTermino = models.TimeField(verbose_name="hora de término")

    def description(self):
        return str(self.descrição)
