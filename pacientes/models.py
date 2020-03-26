from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    tipo_sang = models.CharField(max_length=5, null=False, blank=False)
    cpf = models.CharField(max_length=30, null=False, blank=False)
    data_nasc = models.DateField(max_length=30, null=False, blank=False)
    gener = models.CharField(max_length=30, null=False, blank=False)
    sintomas = models.CharField(max_length=200, null=False, blank=False)
    data_cadastro = models.DateField(null=False, blank=False)
    gravidade_caso = models.CharField(max_length=30, null=False, blank=False)
    descricao_caso = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome

class Preven(models.Model):
    virus = models.CharField(max_length=30, null=False, blank=False)
    prevenir = models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.virus


