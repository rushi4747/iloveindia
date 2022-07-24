# Generated by Django 3.0.2 on 2020-01-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Age', models.IntegerField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
                ('Mobile_No', models.IntegerField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Business_name',
            new_name='Business_Name',
        ),
    ]