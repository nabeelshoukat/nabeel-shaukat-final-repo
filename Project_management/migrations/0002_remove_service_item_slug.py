# Generated by Django 4.1.7 on 2023-03-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_item',
            name='slug',
        ),
    ]
