# Generated by Django 3.2.3 on 2021-06-01 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]