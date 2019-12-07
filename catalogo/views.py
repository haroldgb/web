from django.shortcuts import render
from django.views import generic

from .models import Formulario
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request,'index.html')

def about (request):
    return render(request,'about.html')

def formula (request):
    return render(request,'formulario.html')

def products (request):
    return render(request,'products.html')

def store (request):
    return render(request,'store.html')

class ListaformularioVista(generic.ListView):
    model = Formulario
    context_object_name ='formulario_list' # your own name    for    the    list as    a template    variable
    template_name = 'catalogo/formulario_list.html'


class FormularioCreate(CreateView):
    model = Formulario
    fields = '__all__'


class FormularioUpdate(UpdateView):
    model = Formulario
    fields = ['id','nombre','rut','num_cont','email','mensaje']


class FormularioDelete(DeleteView):
    model = Formulario
    success_url = reverse_lazy('formularios')

class FormularioDetailView(generic.DeleteView):
    model = Formulario

