from web.models import Item
from django.db.models import Q

def list_all_itens():
    itens = Item.objects.all()
    return itens

def search_itens(item, preventiva):
    if preventiva:
        q1 = Q(idSubInventario__startswith='P')
        q2 = Q(descricao__icontains=item)
        itens = Item.objects.filter(q1 & q2)
    else:
        q1 = Q(idSubInventario__startswith='M')
        q2 = Q(descricao__icontains=item)
        itens = Item.objects.filter(q1 & q2)
    return itens

def get_item(item):
    item = Item.objects.get(idSubInventario=item)
    return item
