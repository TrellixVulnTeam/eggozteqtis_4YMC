# Generated by Django 3.1.2 on 2021-09-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0017_auto_20210927_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchmodel',
            name='egg_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='procurement',
            name='additional_charge',
            field=models.FloatField(default=0),
        ),
    ]
