# Generated by Django 5.1.1 on 2024-10-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_alter_product_options_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
