# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operationschain', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationspersonprofile',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='warehouse_operations', to='warehouse.warehouse'),
        ),
    ]
