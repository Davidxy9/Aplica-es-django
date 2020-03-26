from django.shortcuts import render, redirect, get_object_or_404
from pacientes.models import Pessoa, Preven
from pacientes.forms import PessoaForm, PrevenForm


def list(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoa': pessoa})


def create(request):
    form = PessoaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'create.html', {'form': form})


def list1(request):
    preven = Preven.objects.all()
    return render(request, 'list1.html', {'preven': preven})


def create1(request):
    form1 = PrevenForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('list1')
    return render(request, 'create1.html', {'form1': form1})


def virus_update(request, id):
    preven = get_object_or_404(Preven, pk=id)
    form1 = PrevenForm(request.POST or None, instance=preven)
    if form1.is_valid():
        form1.save()
        return redirect('list1')
    return render(request, 'create1.html', {'form1': form1})


def virus_delete(request, id):
    preven = get_object_or_404(Preven, pk=id)
    #form1 = PrevenForm(request.POST or None, instance=preven)
    if request.method == 'POST':
        preven.delete()
        return redirect('list1')
    return render(request, 'preven_delete_confirm.html', {'preven': preven})
