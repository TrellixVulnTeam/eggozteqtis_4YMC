# Generated by Django 3.1.2 on 2021-10-13 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0022_auto_20211013_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='egg_type',
        ),
    ]
