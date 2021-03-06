# Generated by Django 3.2.4 on 2021-06-11 04:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('all', 'Вся Украина'), ('karkov', 'Харьков'), ('kiev', 'Киев'), ('dnepr', 'Днепр'), ('sumy', 'Суммы'), ('ternopol', 'Тернополь'), ('vinica', 'Винница'), ('lvov', 'Львов')], default='all', max_length=50)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('viber', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(blank=True, to='products.Category')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
