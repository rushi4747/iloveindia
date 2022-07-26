# Generated by Django 3.0.2 on 2020-02-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0014_auto_20200217_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default='', max_length=30)),
                ('Address', models.CharField(default='', max_length=30)),
                ('Owner_Name', models.IntegerField(default='0')),
                ('Mobile_No', models.IntegerField(default='0')),
                ('Email', models.CharField(default='', max_length=30)),
                ('Username', models.CharField(default='', max_length=30)),
                ('Password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Mobile_No',
            field=models.IntegerField(default='0'),
        ),
    ]
