# Generated by Django 4.1.5 on 2023-03-06 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0038_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide_image',
            old_name='title',
            new_name='title_name',
        ),
    ]
