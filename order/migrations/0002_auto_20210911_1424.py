# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
        ('distributionchain', '__first__'),
        ('custom_auth', '0002_auto_20210911_1424'),
        ('saleschain', '0001_initial'),
        ('ecommerce', '0002_auto_20210911_1424'),
        ('finance', '__first__'),
        ('product', '0001_initial'),
        ('retailer', '0002_auto_20210911_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderreturnline',
            name='salesPerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='returnSalesPerson', to='saleschain.salespersonprofile'),
        ),
        migrations.AddField(
            model_name='orderpendingtransaction',
            name='beat_assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='distributionchain.beatassignment'),
        ),
        migrations.AddField(
            model_name='orderpendingtransaction',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_pending_transaction', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lines', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='product.product'),
        ),
        migrations.AddField(
            model_name='orderevent',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderevent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='beat_assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='distributionchain.beatassignment'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='OrderCustomer', to='ecommerce.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Orderdistributor', to='distributionchain.distributionpersonprofile'),
        ),
        migrations.AddField(
            model_name='order',
            name='financePerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='OrderfinancePerson', to='finance.financeprofile'),
        ),
        migrations.AddField(
            model_name='order',
            name='packingOrder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.packingorder'),
        ),
        migrations.AddField(
            model_name='order',
            name='primary_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='retailer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='OrderRetailer', to='retailer.retailer'),
        ),
        migrations.AddField(
            model_name='order',
            name='returned_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_returned_bill', to='order.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='salesPerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='OrdersalesPerson', to='saleschain.salespersonprofile'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_orders', to='custom_auth.address'),
        ),
    ]
