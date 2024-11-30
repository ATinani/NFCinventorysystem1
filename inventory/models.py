from django.db import models

CATEGORY = (
    ('Meat', 'Meat'),
    ('SeaFood', 'SeaFood'),
    ('Grains', 'Grains'),
    ('Potatoes', 'Potatoes'),
    ('Fruits&Vegitables', 'Fruits & Vegetables'),
    ('Spices', 'Spices'),
    ('Beverages', 'Beverages'),
    ('BakingEssentials', 'Baking Essentials'),
)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    measurement = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
