# Generated by Django 2.0.13 on 2019-05-03 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tigertravel', '0013_auto_20190502_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sendtime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
