# Generated by Django 4.1.6 on 2023-03-13 20:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_variant_color_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
