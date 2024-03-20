from rest_framework import permissions, viewsets
from .models import Pessoa
from .serializers import PessoaSerializers


class PessoaViewset(viewsets.ModelViewSet):

  queryset = Pessoa.objects.all()
  serializer_class = PessoaSerializers
  

