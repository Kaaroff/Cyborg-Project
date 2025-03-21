from django import forms
from .models import Product, Rating

class ProductCreateForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'user',
            'title',
            'category',
            'main_image',
            'images',
            'description',
            'price',
        )

class ProductUpdateForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'user',
            'title',
            'category',
            'main_image',
            'images',
            'description',
            'price',
        )

