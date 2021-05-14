# Generated by Django 3.2 on 2021-05-04 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('0', 'Все'), ('1', 'Харьков'), ('2', 'Киев'), ('3', 'Днепр'), ('4', 'Суммы'), ('5', 'Тернополь'), ('6', 'Винница'), ('7', 'Львов'), ('8', 'Запоорожье'), ('9', 'Ровно'), ('10', 'Полтава'), ('11', 'Донецк'), ('12', 'Ивано-Франковск'), ('Kharkov', 'Харьков'), ('Kiev', 'Киев'), ('Dnepr', 'Днепр')], default=0, max_length=50)),
                ('contact_whith', models.CharField(choices=[('email', 'email'), ('telegram', 'telegram'), ('viber', 'viber')], default='email', max_length=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='products.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribtions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
