from django.db.models import F
from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField, IntegerField

from Product.models import Product, Category, Supplier
from .serializers import ProductSerializers, SupplierSerializers, CategorySerializers, UserSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'date_joined']
    ordering = ['date_joined']
  

    def get_queryset(self):
        queryset = User.objects.all()  # Start with the full queryset
        filters = {}

        # Get parameters from the request query
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')

        # Dynamically apply filters based on query params
        if username:
            filters['username__icontains'] = username
        if email:
            filters['email__icontains'] = email

        if filters:
            queryset = queryset.filter(**filters) # if all condition is met it takes in the input and use as filters
        
        return queryset # and return the queryset

class ProductInventorySerializer(Serializer):
    name = CharField()
    quantity = IntegerField() 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name']
    ordering_fields = ['name', 'created_at', 'price', 'quantity']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def current_inventory(self, request):
        """
        Retrieve current inventory levels for all products with  filters.
        """
        queryset = self.get_queryset()

        # Apply filters based on query parameters
        category = request.query_params.get('category', None)
        min_price = request.query_params.get('min_price', None)
        max_price = request.query_params.get('max_price', None)
        low_stock = request.query_params.get('low_stock', None)

        try:
            if min_price:
                min_price = float(min_price)    
            if max_price:
                max_price = float(max_price)
            if low_stock:
                low_stock = bool(int(low_stock))
        except ValueError as e:
            raise ValidationError({"detail": str(e)})

        if category:
            queryset = queryset.filter(category__name=category)
        if min_price:
            queryset = queryset.filter(unit_price__gte=float(min_price))
        if max_price:
            queryset = queryset.filter(unit_price__lte=float(max_price))
        if low_stock:
            queryset = queryset.filter(quantity__lte=F('reorder_level'))

        # Use the above serializer to display products and current quantities
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['contact_person', 'email', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
