# Generated by Django 2.2.6 on 2019-10-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
