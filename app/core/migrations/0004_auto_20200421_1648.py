# Generated by Django 3.0.5 on 2020-04-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_covidnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidnews',
            name='href',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covidnews',
            name='title',
            field=models.CharField(max_length=5000),
        ),
    ]