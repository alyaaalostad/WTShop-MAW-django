# Generated by Django 2.2.6 on 2019-10-21 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20191021_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 10, 21, 12, 0, 57, 468295, tzinfo=utc)),
        ),
    ]