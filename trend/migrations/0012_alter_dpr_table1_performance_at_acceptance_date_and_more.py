# Generated by Django 4.1.3 on 2022-12-19 09:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0011_dpr_update_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_ACCEPTANCE_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 12, 19))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_OFFERED_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 12, 19))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_PENDING_TAT_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 12, 19))]),
        ),
        migrations.AlterField(
            model_name='dpr_table1',
            name='PERFORMANCE_AT_REJECTION_DATE',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 12, 19))]),
        ),
    ]