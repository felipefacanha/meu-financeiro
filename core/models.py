from django.db import models
from django.utils import timezone

class Conta(models.Model):
    nome = models.CharField(max_length=100) # Ex: Nubank, Itaú, Carteira
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.nome

class CartaoCredito(models.Model):
    nome = models.CharField(max_length=100)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    dia_fechamento = models.PositiveIntegerField()
    dia_vencimento = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=50, default="bi-list") # Nome do ícone do Bootstrap Icons

    def __str__(self):
        return self.nome

class Lancamento(models.Model):
    TIPO_CHOICES = (
        ('REC', 'Receita'),
        ('DES', 'Despesa'),
        ('TRA', 'Transação'),
    )
    
    data = models.DateField(default=timezone.now)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    cartao = models.ForeignKey(CartaoCredito, on_delete=models.SET_NULL, null=True, blank=True)
    fixa = models.BooleanField(default=False)
    recorrente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} - {self.descricao}"