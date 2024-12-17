from rest_framework import serializers
from .models import Product, Category, Supplier

class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # ['name', 'quantity', 'unit_price', 'supplier', 'description', 'Created_by', 'category' ]

class CategorySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SupplierSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'    