# Generated by Django 4.2.8 on 2023-12-07 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=500, verbose_name='Краткое описания')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('og_type', models.CharField(default='website', max_length=255, verbose_name='Тип Open Graph ссылки')),
                ('og_image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото Open Graph')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=500, verbose_name='Краткое описания')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('bookmarks', models.ManyToManyField(to='collection.bookmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]