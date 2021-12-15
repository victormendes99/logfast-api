from web.models import Item

def list_all_itens():
    itens = Item.objects.all()
    return itens

def search_itens(item, preventiva):
    if preventiva:
        itens = Item.objects.filter(descricao__icontains=item).filter(idSubInventario__startswith='P').order_by('descricao')
    else:
        itens = Item.objects.filter(descricao__icontains=item).filter(idSubInventario__startswith='M').order_by('descricao')    
    return itens

def get_item(item):
    item = Item.objects.get(id=item)
    return item
