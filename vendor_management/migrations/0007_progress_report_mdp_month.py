# Generated by Django 4.1.3 on 2023-04-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management', '0006_vendor_po_approver_upload_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress_report',
            name='MDP_Month',
            field=models.CharField(default='sd', max_length=100),
            preserve_default=False,
        ),
    ]
