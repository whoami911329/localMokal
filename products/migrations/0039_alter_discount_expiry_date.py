# Generated by Django 3.2.3 on 2021-05-20 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_alter_discount_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 19, 10, 4, 20, 541738, tzinfo=utc)),
        ),
    ]