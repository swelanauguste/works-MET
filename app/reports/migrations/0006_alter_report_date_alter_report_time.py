# Generated by Django 5.0.4 on 2024-04-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_alter_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
