from django import forms
from .models import Product
from .utils import ean13_to_dun14


class ProductForm(forms.ModelForm):
    units_number = forms.IntegerField(required=True, min_value=1, label='Units per Container')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        product = super().save(commit=False)
        product.dun14 = ean13_to_dun14(product.ean13, self.cleaned_data['units_number'])
        product.user = self.request.user
        if commit:
            product.save()
        return product

    class Meta:
        model = Product
        fields = ['name', 'description', 'ean13', 'units_number']

