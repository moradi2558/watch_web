# Generated by Django 4.1.6 on 2023-06-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]