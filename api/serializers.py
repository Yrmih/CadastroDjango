from rest_framework import serializers

from .models import Pessoa


# ADICIONADO O DELETE 
class PessoaSerializers(serializers.ModelSerializer): 
    
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'ativo')


# No exemplo acima, delete_url é um novo campo adicionado ao seu serializador que contém a URL para a exclusão de uma pessoa.
# Você precisa configurar a view_name como o nome da view onde você manipula a exclusão (geralmente uma APIView ou ViewSet) e definir o campo lookup_field como o campo pelo qual você identifica os registros a serem excluídos (nesse caso, o id).
# Depois de adicionar o campo delete_url, você precisará definir uma rota em seu urls.py para lidar com a exclusão de pessoas e vincular essa rota ao nome da view fornecido no view_name do campo delete_url em seu serializador.

