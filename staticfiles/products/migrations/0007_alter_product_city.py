# Generated by Django 3.2 on 2021-04-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_discount_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[('0', 'Все'), ('1', 'Харьков'), ('2', 'Киев'), ('3', 'Днепр'), ('4', 'Суммы'), ('5', 'Тернополь'), ('6', 'Винница'), ('7', 'Львов'), ('8', 'Запоорожье'), ('9', 'Ровно'), ('10', 'Полтава'), ('11', 'Донецк'), ('12', 'Ивано-Франковск'), ('Kharkov', 'Харьков'), ('Kiev', 'Киев'), ('Dnepr', 'Днепр')], default=0, max_length=20, verbose_name='Город'),
        ),
    ]