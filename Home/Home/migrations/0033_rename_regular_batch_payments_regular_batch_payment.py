# Generated by Django 4.1.5 on 2023-03-02 11:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0032_regular_batch_payments_alter_dance_session_level_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regular_Batch_Payments',
            new_name='Regular_Batch_Payment',
        ),
    ]