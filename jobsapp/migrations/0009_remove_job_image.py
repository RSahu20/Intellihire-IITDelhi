# Generated by Django 3.2.13 on 2023-07-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0008_auto_20230711_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
    ]