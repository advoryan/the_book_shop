# Generated by Django 2.2 on 2019-05-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190427_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/', verbose_name='Обложка'),
        ),
    ]