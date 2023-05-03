# Generated by Django 4.1.3 on 2022-12-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0005_dpr_table1_delete_dpr_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_ACCEPTANCE_MAIL',
            field=models.FileField(blank=True, null=True, upload_to='dpr_acceptance_mail/'),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_OFFERED_REMARKS',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_PENDING_REASON',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_PENDING_REMARK',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_PENDING_TAT_DATE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_REJECTED_TAT_DATE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dpr_table1',
            name='SOFT_AT_REJECTION_REASON',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PHYSICAL_AT_Status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='Performance_AT_Status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='Soft_AT_Status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
