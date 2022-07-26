# Generated by Django 3.0.2 on 2020-02-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersite', '0023_auto_20200217_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(default='', max_length=100)),
                ('img', models.ImageField(default='', upload_to='usersite/adimg')),
                ('Desc', models.CharField(default='', max_length=30)),
                ('Mobile_No', models.IntegerField(default=0)),
                ('Email', models.EmailField(max_length=50)),
                ('Duration', models.CharField(default='', max_length=30)),
                ('Key', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='E_Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_disc', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Educational',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(default='', max_length=100)),
                ('Img', models.ImageField(default='', upload_to='usersite/placeimg')),
                ('Edu_Disc', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(default='', max_length=30)),
                ('Header', models.CharField(default='', max_length=100)),
                ('Img', models.ImageField(default='', upload_to='usersite/Entimg')),
                ('Ent_Desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.CharField(default='', max_length=500)),
                ('deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default='', max_length=30)),
                ('Date', models.DateField()),
                ('Job_Disc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.CharField(default='', max_length=50)),
                ('Img1', models.ImageField(default='', upload_to='usersite/newsimg')),
                ('Img2', models.ImageField(default='', upload_to='usersite/newsimg')),
                ('News_Disc', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default='', max_length=30)),
                ('Address', models.CharField(default='', max_length=50)),
                ('Owner_name', models.CharField(default='', max_length=30)),
                ('Mobile_No', models.CharField(default='', max_length=10)),
                ('Email', models.EmailField(max_length=50)),
                ('Username', models.CharField(default='', max_length=30)),
                ('Password', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_Name', models.CharField(default='', max_length=30)),
                ('Img1', models.ImageField(default='', upload_to='usersite/placeimg')),
                ('Img2', models.ImageField(default='', upload_to='usersite/placeimg')),
                ('Place_Disc', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=100)),
                ('Video', models.ImageField(default='', upload_to='usersite/Videos')),
                ('Vid_Desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='demoimg',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Mobile_No',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='First_Name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
