from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import UserViewSet, ProductViewSet, CategoryViewSet, SupplierViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')  
router.register(r'products', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', include(router.urls)),  # Automatically generates URL patterns for CRUD actions
    path('products/levels', ProductViewSet.as_view({'get': 'current_inventory'}), name='current_inventory'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]

urlpatterns += router.urls