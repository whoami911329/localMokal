# Generated by Django 3.2 on 2021-05-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_discount_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
