from django.db import models

class Item(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    descricao = models.CharField(max_length=60, null=False, blank=False)
    subInventario = models.CharField(max_length=10, null=False, blank=False)
    endereco = models.CharField(max_length=60, null=False, blank=True)
    estoque = models.IntegerField(null=False, blank=False)
    udm = models.CharField(max_length=2, null=False, blank=False)
    custoUnitario = models.DecimalField(max_digits=6, decimal_places=2)

