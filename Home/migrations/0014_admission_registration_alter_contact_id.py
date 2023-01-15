# Generated by Django 4.1.5 on 2023-01-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_auto_20230108_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission_registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]