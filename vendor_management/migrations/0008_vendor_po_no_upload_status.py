# Generated by Django 4.1.3 on 2023-04-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management', '0007_progress_report_mdp_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_po_No_upload_status',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('update_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
