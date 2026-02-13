from django.shortcuts import render
from .models import Lancamento
from django.db.models import Sum

def lista_gastos(request):
    # Mudamos de Gasto para Lancamento
    lancamentos = Lancamento.objects.all().order_by('-data')
    total_valor = lancamentos.filter(tipo='DES').aggregate(Sum('valor'))['valor__sum'] or 0
    
    return render(request, 'core/lista_gastos.html', {
        'gastos': lancamentos, # Mantivemos o nome da variável no contexto para não quebrar o HTML agora
        'total_valor': total_valor
    })