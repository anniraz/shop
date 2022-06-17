# Generated by Django 4.0.4 on 2022-06-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Название сайта')),
                ('logo', models.ImageField(blank=True, upload_to='images/', verbose_name='Логотип сайта')),
                ('keywords', models.CharField(max_length=255, verbose_name='Ключевые слова для поиска сайта')),
                ('description', models.CharField(max_length=255, verbose_name='Описание сайта')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес сайта')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='телефон')),
                ('email', models.CharField(blank=True, max_length=50)),
                ('facebook', models.CharField(blank=True, help_text='ссылка на facebook', max_length=50)),
                ('instagram', models.CharField(blank=True, help_text='ссылка на instagram', max_length=50)),
                ('twitter', models.CharField(blank=True, help_text='ссылка на twitter', max_length=50)),
                ('telegram', models.CharField(blank=True, help_text='ссылка на telegram', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Основные настройки сайта',
            },
        ),
    ]
