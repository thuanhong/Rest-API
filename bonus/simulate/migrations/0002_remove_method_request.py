# Generated by Django 2.2.2 on 2019-07-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='method',
            name='request',
        ),
    ]
