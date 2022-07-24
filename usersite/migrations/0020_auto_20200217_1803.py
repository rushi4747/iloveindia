# Generated by Django 3.0.2 on 2020-02-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0019_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=30)),
                ('Last_name', models.CharField(default='', max_length=30)),
                ('Age', models.CharField(default='', max_length=10)),
                ('Gender', models.CharField(default='', max_length=30)),
                ('Mobile_No', models.CharField(default='', max_length=10)),
                ('Email', models.CharField(default='', max_length=30)),
                ('Username', models.CharField(default='', max_length=30)),
                ('Password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Org',
        ),
    ]
