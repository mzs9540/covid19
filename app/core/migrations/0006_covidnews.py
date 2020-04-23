# Generated by Django 3.0.5 on 2020-04-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_covidnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('href', models.CharField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]