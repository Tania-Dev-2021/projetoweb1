from pyexpat import model
from django.db import models
from django.contrib import admin


class Dclientes(models.Model):
    nomec=models.CharField(max_length=100)
    cpf=models.CharField(max_length=50)
    endereco=models.TextField()
    tipo_CHOICES=(
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    )
    tipo=models.CharField(max_length=1, choices=tipo_CHOICES)

    def __str__(self):
        return f'{self.nomec}'
        

class Dprodutos(models.Model):
    nomep=models.CharField(max_length=20)
    valor_produto= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nomep}'

class Dpedidos(models.Model):
    status_CHOICES=(
        ('PP', 'PEDIDO EM PROCESSO'),
        ('PR', 'PEDIDO REALIZADO'),
        ('PE', 'PEDIDO ENTREGUE'),
    )
    numero_pedido=models.IntegerField()
    data_pedido=models.DateField(blank=True, null=True)
    cliente=models.ForeignKey(Dclientes, on_delete=models.CASCADE)
    produto=models.ForeignKey(Dprodutos, on_delete=models.CASCADE)
    valor_pedido=models.FloatField()
    status=models.CharField(max_length=2, choices=status_CHOICES)
    quantidade_pedido=models.IntegerField()




