# Generated by Django 4.2.11 on 2024-05-16 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productRegister', '0002_productregistrationmodel_check_product_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productregistrationmodel',
            name='check_product_code',
        ),
    ]
