# Generated by Django 5.0.6 on 2024-07-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("STATIONARY", "STATIONARY"),
                            ("Electronics", "Electronics"),
                            ("Food", "Food"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("quantity", models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
