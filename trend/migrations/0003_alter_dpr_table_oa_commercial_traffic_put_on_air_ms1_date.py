# Generated by Django 4.1.3 on 2022-12-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0002_dpr_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpr_table',
            name='OA_COMMERCIAL_TRAFFIC_PUT_ON_AIR_MS1_DATE',
            field=models.CharField(max_length=100),
        ),
    ]