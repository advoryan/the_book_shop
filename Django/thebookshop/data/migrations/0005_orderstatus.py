# Generated by Django 2.2 on 2019-05-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_series_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(max_length=30, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
    ]
