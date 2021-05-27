# Generated by Django 3.2.3 on 2021-05-16 00:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0019_product_main_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-timestamp',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-timestamp',), 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-timestamp',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='category_img'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[(0, 'Вся Украина'), (1, 'Харьков'), (2, 'Киев'), (3, 'Днепр'), (4, 'Суммы'), (5, 'Тернополь'), (6, 'Винница'), (7, 'Львов'), (8, 'Запоорожье'), (9, 'Ровно'), (10, 'Полтава'), (11, 'Донецк'), (12, 'Ивано-Франковск'), (13, 'Харьков'), (14, 'Киев'), (15, 'Днепр')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='overview',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]