# Generated by Django 4.1.7 on 2023-03-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movielist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('desc', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
