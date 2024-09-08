from django.forms import ModelForm, BooleanField

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

class ReleaseForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
