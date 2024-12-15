from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    quantity = models.IntegerField()
    sku = models.CharField(max_length=5, unique=True)

class Supplier(models.Model):
    quantity = models.IntegerField()
    sku = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True) 



class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    sku = models.CharField(max_length=5, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_query_name='products')
    description = models.TextField(null=True)
    supplier =models.ManyToManyField(Supplier, related_name='supplys')
    Created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='product')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    
    def __str__(self):
        return f'{self.name} in {self.category} category has been created at {self.created_at} by {self.Created_by}' 