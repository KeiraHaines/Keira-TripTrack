# Generated by Django 5.1.1 on 2024-09-12 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_rename_trip_checklistitem_dicttriplst_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklistitem',
            old_name='strItem',
            new_name='title',
        ),
    ]
