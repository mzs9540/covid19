# Generated by Django 3.0.6 on 2020-05-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200506_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldmapcovidstats',
            name='country',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='worldmapcovidstats',
            name='province',
            field=models.CharField(default='None', max_length=100),
        ),
    ]