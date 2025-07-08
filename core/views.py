from django.shortcuts import render, redirect

from item.models import Category, Item, Cover_Image

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    cover_Image = Cover_Image.objects.first()
    
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
        'cover_image': cover_Image

    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    
    else:

        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form,
    })