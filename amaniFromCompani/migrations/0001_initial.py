# Generated by Django 4.2.11 on 2024-05-16 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='amaniProductRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name_in', models.CharField(max_length=200)),
                ('first_last_name_out', models.CharField(max_length=200)),
                ('prudoct_name', models.CharField(max_length=200)),
                ('prudoct_code', models.CharField(blank=True, max_length=200, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='company_product/')),
                ('create', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]