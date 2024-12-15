from rest_framework import serializers
from .models import Product

class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'sku', 'category', 'description', 'supplier'  ]