# Generated by Django 3.2.3 on 2021-07-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_product_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/img/logo.jpg', upload_to='product'),
        ),
    ]