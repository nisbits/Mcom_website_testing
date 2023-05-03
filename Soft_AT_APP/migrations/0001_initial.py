# Generated by Django 4.1.3 on 2023-04-17 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soft_At_Table',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('CIRCLE', models.CharField(max_length=100)),
                ('SITE_ID', models.CharField(max_length=100)),
                ('UNQUI_ID', models.CharField(max_length=100)),
                ('ENODEB_ID', models.CharField(max_length=100, null=True)),
                ('BAND', models.CharField(max_length=100, null=True)),
                ('Circle_Project', models.CharField(max_length=100)),
                ('OEM_NAME', models.CharField(max_length=100, null=True)),
                ('RFAI_DATE', models.DateField(null=True)),
                ('OA_COMMERCIAL_TRAFFIC_PUT_ON_AIR_MS1_DATE', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Date', models.DateField(null=True)),
            ],
        ),
    ]
