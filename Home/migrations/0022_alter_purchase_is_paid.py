# Generated by Django 4.1.5 on 2023-02-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_purchase_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
