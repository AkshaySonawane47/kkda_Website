# Generated by Django 4.1.5 on 2023-03-08 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0042_alter_multipleimage_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multipleimage',
            old_name='images',
            new_name='image',
        ),
    ]