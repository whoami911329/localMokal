# Generated by Django 3.2.1 on 2021-05-10 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribes', '0002_auto_20210505_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribtion',
            old_name='use_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='subscribtion',
            old_name='use_telegram',
            new_name='telegram',
        ),
        migrations.RenameField(
            model_name='subscribtion',
            old_name='use_viber',
            new_name='viber',
        ),
    ]