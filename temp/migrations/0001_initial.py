# Generated by Django 4.0.2 on 2022-08-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
                ('name1', models.IntegerField()),
                ('name2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DogSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50)),
                ('name1', models.IntegerField()),
                ('name2', models.IntegerField()),
            ],
        ),
    ]
