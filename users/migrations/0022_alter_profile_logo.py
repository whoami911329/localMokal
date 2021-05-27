# Generated by Django 3.2.3 on 2021-05-26 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_phone_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='profile_logo', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
