# Generated by Django 4.1.7 on 2023-03-24 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0050_alter_gallery_image_image_category_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]
