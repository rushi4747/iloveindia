# Generated by Django 3.0.2 on 2020-02-19 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0042_auto_20200219_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_portal',
            name='Company_Email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='job_portal',
            name='Mobile_No',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='job_portal',
            name='Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
