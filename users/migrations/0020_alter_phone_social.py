# Generated by Django 3.2.3 on 2021-05-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210527_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='social',
            field=models.CharField(choices=[(0, 'Primary'), (1, 'Telegram'), (2, 'Viber'), (3, 'Whatsup'), (4, 'Facebook')], default=0, max_length=2),
        ),
    ]