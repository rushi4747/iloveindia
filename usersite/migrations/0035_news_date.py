# Generated by Django 3.0.2 on 2020-02-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0034_remove_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Date',
            field=models.DateField(default=22),
            preserve_default=False,
        ),
    ]
