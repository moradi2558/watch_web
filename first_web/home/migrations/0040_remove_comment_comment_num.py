# Generated by Django 4.1.6 on 2023-08-01 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_remove_comment_total_comment_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_num',
        ),
    ]
