# Generated by Django 4.1.6 on 2023-03-15 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
