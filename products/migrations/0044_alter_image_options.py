# Generated by Django 3.2.3 on 2021-05-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_auto_20210520_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('timestamp',), 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]