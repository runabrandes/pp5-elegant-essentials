# Generated by Django 5.1.1 on 2024-10-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Request', 'verbose_name_plural': 'Requests'},
        ),
    ]
