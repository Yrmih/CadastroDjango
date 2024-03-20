from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = "API de Cadastros"
    
    def __str__(self) -> str:
        return super().__str__()
    #devolve uma representação em string do modelo.
    