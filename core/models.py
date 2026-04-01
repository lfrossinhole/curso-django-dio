from django.db import models

# Create your models here.

class Pessoa(models.Model): # Aula 02
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()

# Consulta SQL
# pessoa = Pessoa.objects.get(nome='Rafael')
# select * from pessoa where nome = 'Rafael';