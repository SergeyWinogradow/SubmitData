# Generated by Django 4.1.9 on 2023-06-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(verbose_name='url'),
        ),
    ]