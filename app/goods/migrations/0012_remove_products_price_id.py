# Generated by Django 5.1.1 on 2024-12-02 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_products_price_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price_id',
        ),
    ]
