# Generated by Django 5.1 on 2024-11-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_order_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Meat', 'Meat'), ('SeaFood', 'SeaFood'), ('Grains', 'Grains'), ('Potatoes', 'Potatoes'), ('Fruits&Vegitables', 'Fruits&Vegitables'), ('Spices', 'Spices'), ('Beverages', 'Beverages'), ('BakingEssentials', 'BakingEssentials'), ('Grains', 'Grains')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(choices=[('Meat', 'Meat'), ('SeaFood', 'SeaFood'), ('Grains', 'Grains'), ('Potatoes', 'Potatoes'), ('Fruits&Vegitables', 'Fruits&Vegitables'), ('Spices', 'Spices'), ('Beverages', 'Beverages'), ('BakingEssentials', 'BakingEssentials'), ('Grains', 'Grains')], max_length=20, null=True),
        ),
    ]
