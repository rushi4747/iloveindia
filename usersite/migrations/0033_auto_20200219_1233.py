# Generated by Django 3.0.2 on 2020-02-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0032_auto_20200219_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(),
        ),
    ]
