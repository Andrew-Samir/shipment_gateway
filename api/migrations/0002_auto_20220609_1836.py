# Generated by Django 3.2.5 on 2022-06-09 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('origin', models.CharField(default='', max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('pickup_country', models.CharField(max_length=150, null=True)),
                ('destination_country', models.CharField(max_length=150, null=True)),
                ('service_type', models.CharField(choices=[('same_day', 'Shipped by 10:30 am, delivery by 5 pm.'), ('next_day', 'Guaranteed shipment next day by 5 pm.'), ('express', 'Picked up in one hour, shipped in three hours.'), ('super_rush', 'Pickup within one hour, directly shipped.')], max_length=255, null=True)),
                ('status', models.CharField(choices=[('label_pending', 'Shipment label is pending.'), ('label_rejected', 'Shipment label rejected.'), ('label_ready', 'Shipment label is ready.'), ('pick_up_in_progress', 'Pickup/Drop off in progress.'), ('in_transit', 'Shipment in transit.'), ('out_for_delivery', 'Shipment is out for delivery.'), ('shipped', 'Shipment completed.')], default='label_pending', max_length=255)),
                ('description', models.TextField(default='')),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shipment',
            },
        ),
        migrations.CreateModel(
            name='ShipmentLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_country', models.CharField(max_length=150)),
                ('destination_country', models.CharField(max_length=150)),
                ('amount', models.IntegerField(null=True)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=5)),
                ('comment', models.TextField(default='')),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'shipment_label',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, null=True, unique=True, verbose_name='Email address')),
                ('username', models.CharField(max_length=150, null=True, verbose_name='Username')),
                ('phone', models.CharField(max_length=30, null=True)),
                ('address', models.TextField(default='')),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Courier',
        ),
        migrations.AddField(
            model_name='shipmentlabel',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_label_reciever', to='api.user'),
        ),
        migrations.AddField(
            model_name='shipmentlabel',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_label_sender', to='api.user'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.user'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_label', to='api.shipmentlabel'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_product', to='api.product'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_reciever', to='api.user'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipment_sender', to='api.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.user'),
        ),
    ]