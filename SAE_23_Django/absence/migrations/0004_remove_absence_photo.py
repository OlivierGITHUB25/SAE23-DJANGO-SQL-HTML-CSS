# Generated by Django 4.0.5 on 2022-06-09 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0003_absence_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absence',
            name='photo',
        ),
    ]