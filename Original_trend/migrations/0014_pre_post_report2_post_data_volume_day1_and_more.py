# Generated by Django 4.1.3 on 2023-02-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Original_trend', '0013_rename_post_date_volume_day7_pre_post_report2_post_data_volume_day7_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day1',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day2',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day3',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day4',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day5',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='pre_post_report2',
            name='Post_Data_Volume_Day6',
            field=models.FloatField(blank=True, default=0.0, max_length=100),
        ),
    ]
