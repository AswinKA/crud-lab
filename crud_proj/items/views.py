from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item

@login_required
def dashboard(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})


@login_required
def add_item(request):
    if request.method == "POST":
        Item.objects.create(
            user=request.user,
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price']
        )
        return redirect('dashboard')
    return render(request, 'add_items.html')


@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('dashboard')
    return render(request, 'edit_items.html', {'item': item})



@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id, user=request.user)
    item.delete()
    return redirect('dashboard')
