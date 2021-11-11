# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashfreetransaction',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashfree_transactions_order', to='order.order'),
        ),
        migrations.AddField(
            model_name='cashfreetransaction',
            name='subscriptionRequest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cashfree_transactions_subscription_request', to='ecommerce.subscriptionrequest'),
        ),
        migrations.AddField(
            model_name='cashfreetransaction',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='voucherTransactions', to='ecommerce.rechargevoucher'),
        ),
        migrations.AddField(
            model_name='cashfreetransaction',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='walletTransactions', to='ecommerce.customerwallet'),
        ),
    ]
