# Generated by Django 2.2.2 on 2019-07-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulate', '0003_method_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='request',
            field=models.CharField(default='', max_length=200),
        ),
    ]
