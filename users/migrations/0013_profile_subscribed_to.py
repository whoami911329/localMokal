# Generated by Django 3.2.3 on 2021-05-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_product_slug'),
        ('users', '0012_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribed_to',
            field=models.ManyToManyField(blank=True, to='products.Category'),
        ),
    ]