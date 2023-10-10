from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class SidiaBaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CidadeList(SidiaBaseListView):
    queryset = Cidade.objects.all().order_by('name')
    context_object_name = 'cidades'
    template_name = 'cadastro/lista_cidades.html'


class CidadeDetail(DetailView):
    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastro/detalhe_cidades.html'


class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastro/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastro/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastro/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
