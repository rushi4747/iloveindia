# Generated by Django 3.0.2 on 2020-01-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Customer_Name', models.CharField(max_length=30)),
                ('Mobile_No', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
