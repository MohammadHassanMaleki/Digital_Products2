# Generated by Django 3.2 on 2022-09-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_device_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'ios'), (1, 'web'), (3, 'android')], default=3),
        ),
    ]
