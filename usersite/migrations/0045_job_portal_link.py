# Generated by Django 3.0.2 on 2020-02-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0044_auto_20200219_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_portal',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
    ]
