# Generated by Django 5.0.7 on 2024-08-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='newtrip',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='newtrip',
            name='transport',
        ),
        migrations.AddField(
            model_name='newtrip',
            name='destination',
            field=models.ManyToManyField(to='base.destination'),
        ),
        migrations.AddField(
            model_name='newtrip',
            name='transport',
            field=models.ManyToManyField(to='base.transport'),
        ),
    ]
