# Generated by Django 3.2.4 on 2022-01-28 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_alter_organizer_summercamp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='CampMailId',
        ),
    ]
