# Generated by Django 3.0.2 on 2020-02-19 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0040_remove_news_ndate'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ndate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]