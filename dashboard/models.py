from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
     ('Meat', 'Meat'),
     ('SeaFood', 'SeaFood'),
     ('Grains', 'Grains'),
     ('Potatoes', 'Potatoes'),
     ('Fruits&Vegitables', 'Fruits&Vegitables'),
     ('Spices', 'Spices'),
     ('Beverages', 'Beverages'),
     ('BakingEssentials', 'BakingEssentials'),
     ('Grains', 'Grains'),
     
 )

class Product(models.Model):
    name = models.CharField(max_length=100, null=True) # null=True will be removed when we deploy the system
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)
    measurement = models.CharField(max_length=100, null=True) # null=True will be removed when we deploy the system


    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'