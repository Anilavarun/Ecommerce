# Generated by Django 5.0.7 on 2024-08-30 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cat',
            new_name='categ',
        ),
    ]
