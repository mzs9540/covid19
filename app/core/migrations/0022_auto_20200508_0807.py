# Generated by Django 3.0.6 on 2020-05-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200506_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indiafullcovidstats',
            options={'ordering': ['-total_case'], 'verbose_name_plural': 'India Statewise Covid19 stats'},
        ),
    ]
