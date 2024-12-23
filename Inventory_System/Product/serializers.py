from rest_framework import serializers
from .models import Product, Category, Supplier

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # ['name', 'quantity', 'unit_price', 'supplier', 'description', 'Created_by', 'category' ]
        read_only_fields = ['created_by', 'created_at']  # Make 'created_by' and 'created_at' read-only

    def create(self, validated_data):
        # Get the logged-in user from the request context
        user = self.context['request'].user
        
        # Create the product and associate it with the logged-in user
        product = Product.objects.create(created_by=user, **validated_data)
        return product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'    