# Generated by Django 4.2.3 on 2023-07-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
