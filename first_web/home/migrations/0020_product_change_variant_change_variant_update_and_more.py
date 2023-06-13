# Generated by Django 4.1.6 on 2023-06-13 08:49

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_product_sell_product_total_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='home.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, to='home.size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(default=0)),
                ('update', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pr_update', to='home.product')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='v_update', to='home.variant')),
            ],
        ),
    ]
