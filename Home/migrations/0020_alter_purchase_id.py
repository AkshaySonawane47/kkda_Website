# Generated by Django 4.1.5 on 2023-02-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_remove_purchase_price_purchase_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
