# Generated by Django 3.0.6 on 2020-05-14 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_covid19queryreplies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid19query',
            old_name='reply',
            new_name='admin_reply',
        ),
        migrations.AlterField(
            model_name='covid19queryreplies',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_replies', to='core.Covid19Query'),
        ),
    ]
