# Generated by Django 4.1.5 on 2023-01-09 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_admission_registration_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission_registration',
            old_name='first_name',
            new_name='firstname',
        ),
    ]
