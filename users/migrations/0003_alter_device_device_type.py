# Generated by Django 3.2 on 2022-09-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_device_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'android'), (1, 'web'), (2, 'ios')], default=3),
        ),
    ]
