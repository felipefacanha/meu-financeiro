from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    # Isso faz com que os campos apareçam em colunas na listagem
    list_display = ('data', 'descricao', 'valor', 'categoria', 'fonte_recursos')
    # Adiciona um filtro lateral
    list_filter = ('categoria', 'recorrencia', 'despesa_fixa')
    # Adiciona uma barra de busca
    search_fields = ('descricao', 'categoria')