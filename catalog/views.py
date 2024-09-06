from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from catalog.models import Product
from pytils.translit import slugify
from catalog.forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'category', 'product_image', 'price')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.product_name)
            new_product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return(reverse('catalog:product_detail', args=[self.kwargs.get('pk')]))

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) "{message}"')
        return render(request, 'catalog/contacts.html')


