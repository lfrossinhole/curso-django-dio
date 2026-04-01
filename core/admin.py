from django.contrib import admin
from core.models import Pessoa # Aula 02

# Register your models here.

class PessoaAdmin(admin.ModelAdmin): # Aula 02
    list_display = ('nome', 'idade') # Exibe as colunas nome e idade na lista de pessoas no admin
    list_filter = ('nome',)

admin.site.register(Pessoa, PessoaAdmin) # Registra o modelo Pessoa no admin com a configuração personalizada de PessoaAdmin

