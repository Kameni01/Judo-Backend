# Generated by Django 2.1.4 on 2019-04-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trenercard',
            name='experience',
            field=models.IntegerField(verbose_name='Стаж работы тренером'),
        ),
    ]
