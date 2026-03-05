"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers,permissions
from api_telemetria.api import viewsets
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title= 'Api para telemetria de veiculos agricolas',
        default_version='v1',
        description= 'Sistema para ccadastro e controle por telemetria de frota de veiculos agricolas', 
        erms_of_service= 'https://www.google.com/terms',
        contact=openapi.Contact(email='contato@test.com'), 
        license=openapi.License(name="OpenSource"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

route = routers.DefaultRouter()
route.register(r'marcas', viewsets.MarcaViewset, basename='Marca')
route.register(r'modelos', viewsets.ModeloViewset, basename='Modelo')
route.register(r'unidades-medida', viewsets.UnidadeMedidaViewset, basename='UnidadeMedida')
route.register(r'medicoes', viewsets.MedicaoViewset, basename='Medicao')
route.register(r'veiculos', viewsets.VeiculoViewset, basename='Veiculo')
route.register(r'medicoes-veiculo', viewsets.MedicaoVeiculoViewset, basename='MedicaoVeiculo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]

urlpatterns += [
    path('swaggerjson/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]