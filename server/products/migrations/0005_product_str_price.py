# Generated by Django 5.0.4 on 2024-07-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_primerycategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='str_price',
            field=models.CharField(default=str, max_length=200, verbose_name='قیمت'),
            preserve_default=False,
        ),
    ]
