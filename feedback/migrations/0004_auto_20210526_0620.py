# Generated by Django 3.2.3 on 2021-05-26 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_auto_20210524_1810'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0003_rename_username_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(max_length=600),
        ),
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=600)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]