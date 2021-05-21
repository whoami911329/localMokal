# Generated by Django 3.2.3 on 2021-05-19 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='main_image',
        ),
        migrations.AddField(
            model_name='image',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[('0', 'Вся Украина'), ('1', 'Харьков'), ('2', 'Киев'), ('3', 'Днепр'), ('4', 'Суммы'), ('5', 'Тернополь'), ('6', 'Винница'), ('7', 'Львов'), ('8', 'Запоорожье'), ('9', 'Ровно'), ('10', 'Полтава'), ('11', 'Донецк'), ('12', 'Ивано-Франковск'), ('13', 'Харьков'), ('14', 'Киев'), ('15', 'Днепр')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
