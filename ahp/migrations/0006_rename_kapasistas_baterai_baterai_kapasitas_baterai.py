# Generated by Django 4.0.5 on 2022-09-30 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahp', '0005_remove_smartphone_harga_smartphone_harga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baterai',
            old_name='kapasistas_baterai',
            new_name='kapasitas_baterai',
        ),
    ]
