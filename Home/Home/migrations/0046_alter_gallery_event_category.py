# Generated by Django 4.1.7 on 2023-03-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0045_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='event_Category',
            field=models.ImageField(max_length=50, upload_to=''),
        ),
    ]