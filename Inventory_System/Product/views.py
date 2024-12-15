from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerilizers
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizers
