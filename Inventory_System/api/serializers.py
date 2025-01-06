from rest_framework import serializers
from Product.models import Product, Category, Supplier
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProductSerializers(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username') 

    class Meta:
        model = Product
        fields = '__all__'  # Include all fields
        read_only_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

    def create(self, validated_data):
        """
        Overridden create method to associate the logged-in user with the created product.
        """
        user = self.context['request'].user
        validated_data['created_by'] = user 
        return super().create(validated_data) 
    
    def update(self, instance, validated_data):
        """
        Overridden update method to associate the logged-in user with the updated product.
        """
        user = self.context['request'].user
        validated_data['updated_by'] = user 
        return super().update(instance, validated_data)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'    