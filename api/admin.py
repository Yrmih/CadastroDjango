from django.contrib import admin

# Register your models here.
from .models import Pessoa

admin.site.register(Pessoa)
#Agora, quando você acessar o painel de administração do Django, 
#o modelo cadastroApi estará disponível para ser gerenciado.

