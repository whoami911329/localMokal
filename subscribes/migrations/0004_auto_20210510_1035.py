# Generated by Django 3.2.1 on 2021-05-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribes', '0003_auto_20210510_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribtion',
            name='email',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribtion',
            name='telegram',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='subscribtion',
            name='viber',
            field=models.CharField(default=False, max_length=100),
        ),
    ]