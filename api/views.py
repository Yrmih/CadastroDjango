import requests
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Pessoa
from .serializers import PessoaSerializers

def acessar_endpoint_pessoa(requests):
    # URL do endpoint "pessoa"
    url = "http://127.0.0.1:8000/pessoa/"
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Retornando os dados recebidos do endpoint
        return JsonResponse(response.json())
    else:
        # Retornando um erro caso a requisição não tenha sido bem-sucedida
        return JsonResponse({"erro": "Não foi possível acessar o endpoint pessoa"})

class PessoaDeleteView(generics.DestroyAPIView): # ADICIONADO O DELETE NO VIEWS
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers
    lookup_field = 'id'  # O campo pelo qual você identifica os registros a serem excluídos

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Pessoa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)
