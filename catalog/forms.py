from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product, Release


class StyleFormMixin:
    """
    класс-миксин для стилизации форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-checked-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    """
    форма для создания и редактирования продукта
    """
    class Meta:
        model = Product
        exclude = ('created_at', 'update_at', 'owner')

    def clean_product_name(self):
        """
        валидация поля product_name
        """
        prohibited = ['казино', 'криптовалюта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        product_name = self.cleaned_data['product_name']
        if product_name in prohibited:
            raise ValidationError('запрещенные слова!')
        else:
            return product_name

    def clean_product_description(self):
        """
        валидация поля product_description
        """
        prohibited = ['казино', 'криптовалюта', 'биржа',
                      'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        product_description = self.cleaned_data['product_description']
        if product_description in prohibited:
            raise ValidationError('запрещенные слова!')
        else:
            return product_description

    def clean_is_active(self):
        product = self.instance
        verions = product.version_set.all()
        cleaned_data = self.cleaned_data['is_active']
        if verions.filter(is_active=True).exists() and cleaned_data:
            raise ValidationError('error')
        return cleaned_data


class ModeratorProductForm(ProductForm):

    class Meta:
        model = Product
        fields = ('product_description', 'category')


class ReleaseForm(StyleFormMixin, ModelForm):
    """
    форма версии продукта
    """
    class Meta:
        model = Release
        fields = '__all__'


class ModeratorReleaseForm(ReleaseForm):

    class Meta:
        model = Release
        fields = ('is_active', 'version_name')
