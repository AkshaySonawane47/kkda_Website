# Generated by Django 4.1.7 on 2023-03-25 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0055_alter_score_month_add_scorestudenttable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_scorestudenttable',
            old_name='user',
            new_name='users',
        ),
    ]
