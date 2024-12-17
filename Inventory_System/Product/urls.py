from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, SupplierViewSet
router = DefaultRouter()

# Create a router and register the ViewSets with it
router.register(r'products', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

# Include the router's URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Automatically generates URL patterns for CRUD actions
]