from django.urls import path
from .views import cadastrar_item, listar_itens, editar_item

urlpatterns = [
    path('cadastrar-item', cadastrar_item, name='cadastrar_item'),
    path('listar-itens', listar_itens, name='listar_itens'),
    path('editar-item/<int:itemId>', editar_item, name='editar_item')
]
