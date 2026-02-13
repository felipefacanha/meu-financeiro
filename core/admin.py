from django.contrib import admin
from .models import Conta, CartaoCredito, Categoria, Lancamento

admin.site.register(Conta)
admin.site.register(CartaoCredito)
admin.site.register(Categoria)

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'valor', 'tipo', 'categoria', 'conta')
    list_filter = ('tipo', 'categoria', 'conta')
    search_fields = ('descricao',)