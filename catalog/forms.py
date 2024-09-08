from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product, Release

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance (field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"
                
            

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'update_at')

    def clean_product_name(self):
        prohibited = ['казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        product_name = self.cleaned_data['product_name']
        if product_name in prohibited:
            raise ValidationError('запрещенные слова!')
        else:
            return product_name
        
    def clean_product_description(self):
        prohibited = ['казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        product_description = self.cleaned_data['product_description']
        if product_description in prohibited:
            raise ValidationError('запрещенные слова!')
        else:
            return product_description

class ReleaseForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
