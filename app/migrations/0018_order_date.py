# Generated by Django 2.2.6 on 2019-10-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20191020_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default="1111-11-11"),
            preserve_default=False,
        ),
    ]
