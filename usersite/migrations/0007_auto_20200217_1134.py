# Generated by Django 3.0.2 on 2020-02-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0006_auto_20200217_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default='', max_length=30)),
                ('Address', models.CharField(default='', max_length=30)),
                ('Owner_Name', models.CharField(default='', max_length=30)),
                ('Email', models.CharField(default='', max_length=30)),
                ('Username', models.CharField(default='', max_length=30)),
                ('Password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='slideimg',
        ),
    ]
