# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.db import migrations, models
import django.db.models.deletion
import uuid_upload_path.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '__first__'),
        ('ecommerce', '0002_auto_20210911_1424'),
        ('distributionchain', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(max_length=254)),
                ('file', models.FileField(blank=True, null=True, upload_to=uuid_upload_path.storage.upload_to)),
                ('invoice_due', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('invoice_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled'), ('Adjusted', 'Adjusted'), ('Waiveoff', 'Waiveoff'), ('Bad debt', 'Bad debt')], default='Pending', max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_received', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('UPI', 'UPI')], max_length=200)),
                ('payment_mode', models.CharField(default='PETTY CASH', max_length=200)),
                ('pay_choice', models.CharField(choices=[('InstantPay', 'InstantPay'), ('LaterPay', 'LaterPay'), ('Refund', 'Refund'), ('Replacement', 'Replacement'), ('Return', 'Return')], default='InstantPay', max_length=200)),
                ('cheque_number', models.CharField(blank=True, max_length=200, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('salesTransaction__transaction_date',),
            },
        ),
        migrations.CreateModel(
            name='SalesTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=254, null=True)),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit'), ('Refund', 'Refund'), ('Return', 'Return'), ('Promo', 'Promo'), ('Replacement', 'Replacement'), ('Debit Note', 'Debit Note'), ('Adjusted', 'Adjusted'), ('Cancelled', 'Cancelled')], max_length=200)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('transaction_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('remarks', models.CharField(max_length=254, null=True)),
                ('current_balance', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_trial', models.BooleanField(default=False)),
                ('beat_assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='distributionchain.beatassignment')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_transaction', to='ecommerce.customer')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='distributor_transaction', to='distributionchain.distributionpersonprofile')),
                ('financePerson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='finance_transaction', to='finance.financeprofile')),
                ('invoices', models.ManyToManyField(blank=True, related_name='sales_invoices', to='payment.Invoice')),
            ],
            options={
                'ordering': ['transaction_date', 'id'],
            },
        ),
    ]
