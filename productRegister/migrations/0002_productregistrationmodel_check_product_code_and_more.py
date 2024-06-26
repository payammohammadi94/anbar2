# Generated by Django 4.2.7 on 2024-05-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productRegister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productregistrationmodel',
            name='check_product_code',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='productregistrationmodel',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='company_product/'),
        ),
    ]
