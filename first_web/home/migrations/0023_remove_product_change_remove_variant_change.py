# Generated by Django 4.1.6 on 2023-07-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='change',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='change',
        ),
    ]
