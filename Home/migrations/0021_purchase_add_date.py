# Generated by Django 4.1.5 on 2023-02-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_alter_purchase_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
