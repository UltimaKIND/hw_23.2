from django.db.models.base import Model as Model
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from catalog.models import Product, Release
from catalog.forms import ProductForm, ReleaseForm, ModeratorProductForm, ModeratorReleaseForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.services import get_products_from_cache


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    контроллер для страницы создания нового продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ReleaseFormset = inlineformset_factory(
            Product, Release, ReleaseForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ReleaseFormset(
                self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ReleaseFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            product = form.save()
            product.owner = self.request.user
            product.save()
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    контроллер для страницы редактирования продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return (reverse('catalog:product_detail', args=[self.kwargs.get('pk')]))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser:
            ReleaseFormset = inlineformset_factory(
                Product, Release, ReleaseForm, extra=1)
        else:
            ReleaseFormset = inlineformset_factory(
                Product, Release, ModeratorReleaseForm, extra=1, can_delete=False)
        if self.request.method == 'POST':
            context_data['formset'] = ReleaseFormset(
                self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ReleaseFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid() and formset.is_valid():
            product = form.save()
            product.owner = self.request.user
            product.save()
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if self.request.user.is_superuser:
            return ProductForm
        if user.has_perm('catalog.change_product') or self.object.owner == user:
            return ModeratorProductForm
        raise PermissionDenied


class ProductListView(ListView):
    """
    контроллер для страницы отображения списка продуктов
    """
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    """
    контроллер для страницы детального отображения продукта
    """
    model = Product


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """
    контроллер для страницы подтверждения удаления продукта
    """
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsPageView(TemplateView):
    """
    контроллер для страницы контактов
    """
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) "{message}"')
        return render(request, 'catalog/contacts.html')
