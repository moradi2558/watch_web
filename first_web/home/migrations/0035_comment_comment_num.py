# Generated by Django 4.1.6 on 2023-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_remove_comment_comment_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]