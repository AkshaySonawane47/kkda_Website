# Generated by Django 4.1.7 on 2023-03-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0053_score_attendence_score_duration_score_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='Total_days',
            field=models.IntegerField(default='31'),
        ),
        migrations.AddField(
            model_name='score',
            name='month',
            field=models.CharField(default=22, max_length=20),
            preserve_default=False,
        ),
    ]