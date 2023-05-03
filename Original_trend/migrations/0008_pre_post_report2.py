# Generated by Django 4.1.3 on 2023-02-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Original_trend', '0007_pre_post_report_post_trend_cell_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pre_post_report2',
            fields=[
                ('Post_cell_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Post_cell_site_id', models.CharField(blank=True, max_length=100)),
                ('Post_trend_cell', models.CharField(blank=True, max_length=100)),
                ('Pre_cell_name', models.CharField(blank=True, max_length=100)),
                ('Pre_cell_site_id', models.CharField(blank=True, max_length=100)),
                ('Pre_trend_cell', models.CharField(blank=True, max_length=100)),
                ('Pre_offered_date', models.DateField()),
                ('Post_offered_date', models.DateField()),
                ('Pre_Volte_Traffic_Day1', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day2', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day3', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day4', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day5', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day6', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Volte_Traffic_Day7', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day1', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day2', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day3', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day4', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day5', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day6', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Volte_Traffic_Day7', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day1', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day2', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day3', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day4', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day5', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day6', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Pre_Date_Volume_Day7', models.FloatField(blank=True, default=0.0, max_length=100)),
                ('Post_Date_Volume_Day7', models.FloatField(blank=True, default=0.0, max_length=100)),
            ],
        ),
    ]