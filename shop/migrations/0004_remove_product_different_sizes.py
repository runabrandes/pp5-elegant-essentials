# Generated by Django 5.1.1 on 2024-10-07 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='different_sizes',
        ),
    ]
