# Generated by Django 5.1.2 on 2024-11-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default=True, max_length=11, unique=True, verbose_name='شماره تلفن'),
        ),
    ]