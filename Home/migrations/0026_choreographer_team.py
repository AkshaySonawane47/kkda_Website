# Generated by Django 4.1.5 on 2023-02-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0025_order_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choreographer_Team',
            fields=[
                ('C_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('Work_roll', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='contents/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
