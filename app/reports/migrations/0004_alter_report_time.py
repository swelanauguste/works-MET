# Generated by Django 5.0.4 on 2024-04-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_rr_time_alter_report_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
