# Generated by Django 5.0.7 on 2024-08-28 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_newtrip_strtripname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg',
            name='destination',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.destination'),
        ),
    ]
