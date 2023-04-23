from django.db import models


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    tipo_material = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
