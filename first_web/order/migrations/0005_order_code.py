# Generated by Django 4.1.6 on 2023-06-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_coupon_end_alter_coupon_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
