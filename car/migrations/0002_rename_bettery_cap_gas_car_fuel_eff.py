# Generated by Django 5.0.1 on 2024-02-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gas_car',
            old_name='bettery_cap',
            new_name='fuel_eff',
        ),
    ]
