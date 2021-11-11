# Generated by Django 3.1.2 on 2021-09-11 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retailer', '0001_initial'),
        ('custom_auth', '0002_auto_20210911_1424'),
        ('saleschain', '0001_initial'),
        ('base', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer',
            name='onboarded_salesPerson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='onBoardedSalesPerson', to='saleschain.salespersonprofile'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='payment_cycle',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='retailer.retailerpaymentcycle'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='retailer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retailer',
            name='retailerBeat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retailerBeat', to='retailer.retailerbeat'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='salesPersonProfile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesPersonProfile', to='saleschain.salespersonprofile'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.sector'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retailer_shipping_address', to='custom_auth.address'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='short_name',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='retailer.retailershorts'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='retailer.customer_subcategory'),
        ),
        migrations.AddField(
            model_name='marginrates',
            name='margin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='margin_commission', to='retailer.commissionslab'),
        ),
        migrations.AddField(
            model_name='marginrates',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='margin_product', to='product.product'),
        ),
        migrations.AlterUniqueTogether(
            name='discountslab',
            unique_together={('white_number', 'brown_number', 'nutra_number', 'type')},
        ),
        migrations.AddField(
            model_name='customer_subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='retailer.customer_category'),
        ),
        migrations.AddField(
            model_name='commissionslab',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.city'),
        ),
        migrations.AlterUniqueTogether(
            name='customer_subcategory',
            unique_together={('name', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='commissionslab',
            unique_together={('number', 'type')},
        ),
    ]
