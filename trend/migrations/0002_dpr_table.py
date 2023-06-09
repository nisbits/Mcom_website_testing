# Generated by Django 4.1.3 on 2022-12-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DPR_table',
            fields=[
                ('SITE_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('CIRCLE', models.CharField(max_length=100)),
                ('Unique_SITE_ID', models.CharField(max_length=100)),
                ('BAND', models.CharField(max_length=100)),
                ('TOCO_NAME', models.CharField(max_length=255)),
                ('OA_COMMERCIAL_TRAFFIC_PUT_ON_AIR_MS1_DATE', models.DateField()),
                ('Project', models.CharField(max_length=100)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('PHYSICAL_AT_Status', models.CharField(max_length=100)),
                ('Soft_AT_Status', models.CharField(max_length=100)),
                ('Performance_AT_Status', models.CharField(max_length=100)),
            ],
        ),
    ]
