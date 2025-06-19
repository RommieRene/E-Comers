from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Item
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from django.http import JsonResponse

def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    browse=Item.objects.filter(is_sold=False)

    if category_id:
        browse = browse.filter(category_id=category_id)
        print("if_1 :",browse)

    if query:
        browse = browse.filter(Q(name__icontains=query) | Q(descroption__icontains=query))
        print("if_2",browse)
    # return json.dumps({'items': browse,
    #     'query': query,
    #     'categories': categories,
    #     'category_id': int(category_id)
    # })
    items_data = [{
        'id': item.id,
        'name': item.name,
        'description': item.descroption,
        'price': item.price,
        'image': item.image.url if item.image else None,
        'category': item.category.name,
        'is_sold': item.is_sold,
        'created_by': item.created_by.username,
        'created_at': item.created_at.isoformat()
    } for item in browse]

    # Serialize categories
    categories_data = [{
        'id': cat.id,
        'name': cat.name
    } for cat in categories]

    return JsonResponse({
        'items': items_data,
        'query': query,
        'categories': categories_data,
        'category_id': int(category_id)
    })

def detail(request, pk):
    
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })


@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
