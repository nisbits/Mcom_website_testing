# Generated by Django 4.1.3 on 2023-02-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Original_trend', '0020_remove_pre_post_report2_post_trend_cell_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_post_report2',
            name='Blank',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]