# Generated by Django 4.0.5 on 2022-09-27 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahp', '0004_remove_smartphone_brand_smartphone_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='harga',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='harga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ahp.harga'),
        ),
    ]