from web.models import Item

def list_all_itens():
    itens = Item.objects.all()
    return itens

def search_itens(item, preventiva):
    if preventiva:
        itens = Item.objects.filter(idSubInventario__startswith='P', descricao__icontains=item).order_by('descricao')
    else:
        itens = Item.objects.filter(idSubInventario__startswith='M', descricao__icontains=item).order_by('descricao')    
    return itens

def get_item(item):
    item = Item.objects.get(idSubInventario=item)
    return item
