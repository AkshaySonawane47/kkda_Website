# Generated by Django 4.1.5 on 2023-03-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0034_remove_regular_batch_payment_amount_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order_form',
            new_name='form',
        ),
        migrations.AlterField(
            model_name='regular_batch_payment',
            name='Remaining',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
