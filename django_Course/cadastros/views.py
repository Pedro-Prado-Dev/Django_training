from django.contrib.auth.decorators import login_required
# from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class SidiaBaseListView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['titulo'] = 'Projeto SIDIA'
        return context


class CidadeList(SidiaBaseListView):
    queryset = Cidade.objects.all().order_by('name')
    context_object_name = 'cidades'
    template_name = 'cadastro/lista_cidades.html'


# class CidadeList(View):
#     def get(self, request):
#         qs = Cidade.objects.all().order_by('name')
#
#         context = {
#             'cidades': qs,
#             'titulo': 'SIDIA'
#         }
#
#         return render(request, 'cadastro/lista_cidades.html', context)

# def post(self, request):
#     pass

# def lista_cidades(request):
#     qs = Cidade.objects.all().order_by('name')
#
#     context = {
#         'cidades': qs,
#         'titulo': 'SIDIA'
#     }
#
#     return render(request, 'cadastro/lista_cidades.html', context)


def detalhe_cidade(request, id):
    cidade = get_object_or_404(Cidade, pk=id)

    context = {
        'cidade': cidade,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastro/detalhe_cidades.html', context)


@login_required
def cadastra_cidade(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cidades-list')

    else:
        form = CidadeForm()

    context = {
        'form': form,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastro/cadastra_cidades.html', context)


@login_required
def remove_cidade(request, id):
    # if not request.user.is_authenticated:
    #     raise PermissionDenied

    cidade = get_object_or_404(Cidade, pk=id)
    cidade.delete()

    return redirect('cidades-list')


@login_required
def editar_cidade(request, id):
    cidade_objeto = get_object_or_404(Cidade, pk=id)
    form = CidadeForm(request.POST or None, instance=cidade_objeto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cidades-list')

    context = {
        'form': form,
        'Titulo': 'SIDIA',
        'obj': cidade_objeto
    }
    return render(request, 'cadastro/edita_cidades.html', context)
