from django.db import models

# Create your models here.
class Funcionario(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    admissao = models.DateField()

    class Meta:
        app_label = 'rescisap_app'

    def __str__(self):
        return self.nome
    