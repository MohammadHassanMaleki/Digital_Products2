# Generated by Django 3.2 on 2022-09-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'web'), (3, 'android'), (2, 'ios')], default=3),
        ),
    ]
