from django import forms 
from .models import Product, Category
#from django.db import models

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['category', 'slug', 'name','price','description','image']