# Generated by Django 2.2.3 on 2019-07-03 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_products_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
