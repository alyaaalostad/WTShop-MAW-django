# Generated by Django 2.2.6 on 2019-10-21 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20191021_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 21, 11, 59, 35, 4078, tzinfo=utc)),
        ),
    ]
