# Generated by Django 5.0.1 on 2024-02-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_remove_contact_adress_remove_contact_instagram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='لینک بیج اینستا'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن'),
        ),
    ]