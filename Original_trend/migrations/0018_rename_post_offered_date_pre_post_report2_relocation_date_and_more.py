# Generated by Django 4.1.3 on 2023-02-16 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Original_trend', '0017_pre_post_report2_percentage_change_data_volume_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pre_post_report2',
            old_name='Post_offered_date',
            new_name='Relocation_date',
        ),
        migrations.RenameField(
            model_name='pre_post_report2',
            old_name='Pre_offered_date',
            new_name='Today_date',
        ),
    ]