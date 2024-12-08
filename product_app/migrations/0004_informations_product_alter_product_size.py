# Generated by Django 5.1.3 on 2024-12-08 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_informations'),
    ]

    operations = [
        migrations.AddField(
            model_name='informations',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informations', to='product_app.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='products', to='product_app.size'),
        ),
    ]