# Generated by Django 5.0.6 on 2024-05-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=150, verbose_name='Страна')),
                ('country_description', models.TextField(blank=True, verbose_name='Описание страны')),
                ('country_photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото страны')),
                ('city_name', models.CharField(default='Russia', max_length=150, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.CharField(default='Ufa', max_length=150, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.CharField(default='Russia', max_length=150, verbose_name='Страна'),
        ),
    ]
