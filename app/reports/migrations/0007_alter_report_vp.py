# Generated by Django 5.0.4 on 2024-04-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_alter_report_date_alter_report_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='vp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
