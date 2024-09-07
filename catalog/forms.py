from django.forms import ModelForm

from catalog.models import Product, Release

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'update_at')

class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
