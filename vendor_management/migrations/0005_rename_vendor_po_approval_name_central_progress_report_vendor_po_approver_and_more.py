# Generated by Django 4.1.3 on 2023-04-08 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management', '0004_upload_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress_report',
            old_name='Vendor_PO_Approval_Name_Central',
            new_name='Vendor_PO_Approver',
        ),
        migrations.RenameField(
            model_name='progress_report',
            old_name='Vendor_PO_Approval_Name_Circle',
            new_name='Vendor_PO_Requestor',
        ),
    ]