# Generated by Django 3.2.3 on 2021-05-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_rename_overview_discount_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
