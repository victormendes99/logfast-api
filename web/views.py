from django.shortcuts import redirect, render
from .forms import item_form
from .models import Item

def cadastrar_item(request):
    if request.method == "POST":
        form_item = item_form.ItemForm(request.POST, request.FILES)
        if form_item.is_valid():
            form_item.save()
            return redirect('listar_itens')
    else:
        form_item = item_form.ItemForm()
    return render(request, 'form_item.html', {'form_item': form_item})

def listar_itens(request):
    itens = Item.objects.all()
    return render(request, 'lista_itens.html', {'itens': itens})

def editar_item(request, itemId):
    item = Item.objects.get(id=itemId)
    form_item = item_form.ItemForm(request.POST or None, instance=item)
    if form_item.is_valid():
        form_item.save()
        return redirect('listar_itens')
    return render(request, 'form_item.html', {'form_item': form_item})