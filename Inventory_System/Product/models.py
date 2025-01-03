from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import F, Q
# Create your models here.

# Import User
User = get_user_model()
# category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Unnamed")
    description = models.TextField(blank=True, default="")   

    def __str__(self):
        return self.name
# Supplier
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Unnamed")
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

# Product
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_query_name='products')
    description = models.TextField(null=True)
    supplier =models.ForeignKey(Supplier,on_delete=models.SET_NULL, null=True, related_name='supply')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_updated')
    sku = models.CharField(max_length=50, unique=True, default='DEFAULT_SKU')  # Stock Keeping Unit
    reorder_level = models.PositiveIntegerField(default=0)  # Minimum stock level

    def save(self, *args, **kwargs):
        if not self.updated_by:
            self.updated_by = self.created_by # Makes the Creator The Updater automatically untill the updater is set
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f'{self.name} in {self.category} category has been created at {self.created_at} by {self.created_by}'

 
    
    def is_low_stock(self):
        return self.quantity <= self.reorder_level # quantity is smaller or equal to the reorder level of each product
    
    @classmethod
    def check_and_notify_low_stock(cls):
        """Class method to check and notify low-stock products."""
        low_stock_products = cls.objects.filter(Q(quantity__lte=F("reorder_level")))
        for product in low_stock_products:
            generate_low_stock_alert(product)

# Utility function for low-stock alert
def generate_low_stock_alert(product):
    """Generate an alert for a low-stock product."""
    print(
        f"Alert: {product.name} is low on stock. Current quantity: {product.quantity}, Reorder level: {product.reorder_level}."
    )