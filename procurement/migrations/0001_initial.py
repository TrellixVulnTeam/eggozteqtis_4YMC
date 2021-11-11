# Generated by Django 3.1.2 on 2021-09-16 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import procurement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chatki', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('intact', models.IntegerField(default=0)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.CharField(db_index=True, default=procurement.models.batch_generator, max_length=15, unique=True)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('egg_count', models.IntegerField(default=0)),
                ('quality_param1', models.CharField(max_length=100, null=True)),
                ('quality_param2', models.CharField(max_length=100, null=True)),
                ('quality_param3', models.CharField(max_length=100, null=True)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnedPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=20)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='procurement.package')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementPerWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='procurement.procurement')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='batch_id',
            field=models.ForeignKey(db_column='batch_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='procurement.procurement'),
        ),
        migrations.AddField(
            model_name='package',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EggsIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('egg_count', models.IntegerField(default=0)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('batch_id', models.ForeignKey(db_column='batch_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='batch_eggsin_set', to='procurement.procurement')),
                ('procurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='procurement_eggsin_set', to='procurement.procurement')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EggQualityCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chatki', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('intact', models.IntegerField(default=0)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=20)),
                ('batch_id', models.ForeignKey(db_column='batch_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='procurement.procurement')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EggCleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chatki', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('intact', models.IntegerField(default=0)),
                ('egg_type', models.CharField(choices=[('White', 'White'), ('Brown', 'Brown')], max_length=20)),
                ('batch_id', models.ForeignKey(db_column='batch_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='procurement.procurement')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
