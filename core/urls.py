"""
Configuração de URL para o projeto principal.

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Visualizações de função
    1. Adicione uma importação: das visualizações de importação my_app
    2. Adicione um URL aos urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
    1. Adicione uma importação: from other_app.views import Home
    2. Adicione um URL aos urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicione um URL aos urlpatterns: path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from api import veiwsets
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('pessoa', veiwsets.PessoaViewset)

# Crie a view de esquema usando drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

# URLs para Swagger usando drf-yasg
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Adicione as URLs do router padrão
urlpatterns += router.urls
