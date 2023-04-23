from django.shortcuts import render
from .models import Material

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')


def materiais(request):
    # Salvando informações do Formulário
    novo_material = Material()
    novo_material.nome = request.POST.get('nome')
    novo_material.valor = request.POST.get('valor')
    novo_material.peso = request.POST.get('peso')
    novo_material.quantia = request.POST.get('quantia')
    novo_material.tipo_material = request.POST.get('tipo_material')
    novo_material.descricao = request.POST.get('descricao')
    novo_material.save()
    # Exibir dados
    materiais = {
        'materiais': Material.objects.all()
    }
    # Retorno dos dados para a página
    return render(request,'usuarios/materiais.html',materiais)
