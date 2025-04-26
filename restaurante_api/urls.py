from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from restaurante.views import (
    RestauranteViewSet,
    PedidoViewSet,
    PizzaViewSet,
    ItemPedidoViewSet,
)

schema_view = get_schema_view(
    openapi.Info(
        title="API da Pizzaria",
        default_version='v1',
        description="Documentação da API da pizzaria com pedidos e cardápio 🍕",
        contact=openapi.Contact(email="contato@pizzaria.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'pizzas', PizzaViewSet)
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itens-pedido', ItemPedidoViewSet)

urlpatterns = [
    path('', lambda request: redirect('schema-swagger-ui')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
