# Generated by Django 4.1.5 on 2023-01-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_alter_post_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]