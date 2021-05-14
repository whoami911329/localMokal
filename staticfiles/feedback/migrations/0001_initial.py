# Generated by Django 3.2 on 2021-05-02 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
