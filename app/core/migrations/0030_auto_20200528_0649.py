# Generated by Django 3.0.6 on 2020-05-28 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20200514_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worldcovidstats',
            options={'ordering': ['-total_case'], 'verbose_name_plural': 'World Covid19 Stats'},
        ),
    ]
