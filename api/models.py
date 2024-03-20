from typing import Any
from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome 
    #colocando o softdelete.
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        return super().delete(using, keep_parents)