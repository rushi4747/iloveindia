# Generated by Django 3.0.2 on 2020-02-19 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0039_auto_20200219_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='ndate',
        ),
    ]
