# Generated by Django 5.0.1 on 2024-02-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')),
                ('f_name', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('l_name', models.CharField(max_length=200, null=True, verbose_name='نام خانوادگی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='ایمیل')),
                ('phone', models.IntegerField(verbose_name='شماره تلفن')),
                ('f_name', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('l_name', models.CharField(max_length=200, null=True, verbose_name='نام خانوادگی')),
                ('password', models.CharField(max_length=16, verbose_name='رمز عبور')),
                ('password_conf', models.CharField(max_length=16, verbose_name='رمز تایید شده')),
                ('otp_code', models.IntegerField(verbose_name='کد اعتبار سنجی')),
                ('expiration', models.DateTimeField(auto_now_add=True, verbose_name='زمان اعتبار سنجی')),
                ('token', models.CharField(max_length=100, unique=True, verbose_name='توکن')),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]
