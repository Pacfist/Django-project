# Generated by Django 5.1.1 on 2024-11-26 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]