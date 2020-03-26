from django.forms import ModelForm
from pacientes.models import Pessoa, Preven


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'tipo_sang', 'cpf', 'data_nasc', 'gener', 'sintomas', 'data_cadastro', 'gravidade_caso', 'descricao_caso']


class PrevenForm(ModelForm):
    class Meta:
        model = Preven
        fields = ['virus', 'prevenir']