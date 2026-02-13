from django.db import models
from django.utils import timezone

class Gasto(models.Model):
    CHOICES_SIM_NAO = (('S', 'Sim'), ('N', 'Não'))
    
    data = models.DateField(default=timezone.now)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    recorrencia = models.CharField(max_length=1, choices=CHOICES_SIM_NAO)
    despesa_fixa = models.CharField(max_length=1, choices=CHOICES_SIM_NAO)
    fonte_recursos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.data} - {self.descricao} (R$ {self.valor})"