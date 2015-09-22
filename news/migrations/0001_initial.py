# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa Kategorii')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Odnośnik')),
                ('icon', models.ImageField(blank=True, verbose_name='Ikona Kategorii', upload_to='icons')),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
                'verbose_name': 'Kategoria',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Odnośnik')),
                ('text', models.TextField(verbose_name='Treść')),
                ('posted_date', models.DateTimeField(verbose_name='Data dodania', auto_now_add=True)),
                ('categories', models.ManyToManyField(verbose_name='Kategorie', to='news.Category')),
            ],
            options={
                'verbose_name_plural': 'Wiadomośći',
                'verbose_name': 'Wiadomość',
            },
        ),
    ]
