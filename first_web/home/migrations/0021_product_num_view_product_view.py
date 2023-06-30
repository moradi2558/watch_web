# Generated by Django 4.1.6 on 2023-06-30 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0020_product_change_variant_change_variant_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.ManyToManyField(blank=True, related_name='product_view', to=settings.AUTH_USER_MODEL),
        ),
    ]
