# Generated by Django 5.0.1 on 2024-02-14 18:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_rename_titile_comment_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, verbose_name='نام')),
                ('l_name', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='شماره تلفن')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('postal_code', models.CharField(max_length=20, verbose_name='کد بستی')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آبدیت شده')),
                ('paid', models.BooleanField(default=False, verbose_name='وضعیت پرداخت')),
                ('total_price', models.BigIntegerField(verbose_name='قیمت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(verbose_name='قیمت')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('color', models.CharField(max_length=200, verbose_name='رنگ')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product', verbose_name='محصولات سفارش')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-created'], name='orders_orde_created_743fca_idx'),
        ),
    ]
