# Generated by Django 3.2.3 on 2021-05-23 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='start_date',
        ),
    ]
