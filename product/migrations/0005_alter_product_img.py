# Generated by Django 5.0.7 on 2024-08-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_cat_categ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(max_length=9999),
        ),
    ]