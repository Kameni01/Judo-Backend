# Generated by Django 2.1.4 on 2019-04-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_news_anons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.CharField(choices=[(0, 'Новость'), (1, 'Грядущее событие')], default=0, max_length=50, verbose_name='Вид события'),
        ),
    ]