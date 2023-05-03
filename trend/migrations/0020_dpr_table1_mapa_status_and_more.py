# Generated by Django 4.1.3 on 2023-01-01 19:54

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0019_remove_dpr_table1_performance_at_rejected_tat_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dpr_table1',
            name='MAPA_STATUS',
            field=models.CharField(blank=True, default='NOT OK', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_PENDING_TAT_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PHYSICAL_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PHYSICAL_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PHYSICAL_AT_PENDING_TAT_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PHYSICAL_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='SOFT_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='SOFT_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='SOFT_AT_PENDING_TAT_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='SOFT_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='performance_at_table',
            name='PERFORMANCE_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='performance_at_table',
            name='PERFORMANCE_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
        migrations.AlterField(
            model_name='performance_at_table',
            name='PERFORMANCE_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 1, 2))]),
        ),
    ]