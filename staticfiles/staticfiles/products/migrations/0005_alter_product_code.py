# Generated by Django 3.2 on 2021-04-16 21:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210416_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=8, null=True, unique=True),
        ),
    ]
