# Generated by Django 3.2.3 on 2021-05-19 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20210519_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 19, 12, 53, 21389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
