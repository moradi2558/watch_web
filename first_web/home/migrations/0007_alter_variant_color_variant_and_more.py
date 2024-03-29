# Generated by Django 4.1.6 on 2023-03-13 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='color_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.color'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.size'),
        ),
    ]
