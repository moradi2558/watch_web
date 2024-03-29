# Generated by Django 4.1.6 on 2023-03-15 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='product_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='unlike',
            field=models.ManyToManyField(blank=True, related_name='product_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
