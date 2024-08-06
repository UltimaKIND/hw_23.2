from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from catalog.models import Product

class ProductListView(ListView):
    model = Product 

class ProductDetailView(DetailView):
    model = Product

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')

    return render(request, 'catalog/contacts.html')

