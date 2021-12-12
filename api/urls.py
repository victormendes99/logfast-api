from django.urls import path
from .views import AllItensList, SearchItensList, getItem

urlpatterns = [
    path('search-itens', SearchItensList.as_view(), name='search_itens'),
    path('listar-itens', AllItensList.as_view(), name='listar_itens'),
    path('item', getItem.as_view(), name='item'),
]
