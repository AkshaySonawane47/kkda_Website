# Generated by Django 4.1.5 on 2023-03-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0039_rename_title_slide_image_title_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choreography_team',
            name='image',
            field=models.FileField(upload_to='contents/'),
        ),
    ]
