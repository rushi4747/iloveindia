# Generated by Django 3.0.2 on 2020-02-17 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0020_auto_20200217_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Age',
        ),
    ]