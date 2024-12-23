from rest_framework import viewsets, filters, permissions, pagination

from .models import Product, Category, Supplier
from .serializers import ProductSerializers, SupplierSerializers, CategorySerializers
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name']
    ordering_fields = ['name', 'created_at', 'price', 'quantity']
    ordering = ['-created_at']

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    