# Generated by Django 4.2.3 on 2023-07-19 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('customer', '0002_customer_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='room',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.PROTECT, to='room.room'),
        ),
    ]