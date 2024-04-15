# Generated by Django 5.0.4 on 2024-04-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='date_time',
        ),
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]