# Generated by Django 4.1.6 on 2023-06-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='DefaultUser.webp', upload_to='profile'),
        ),
    ]
