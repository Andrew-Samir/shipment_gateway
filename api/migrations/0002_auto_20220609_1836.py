# Generated by Django 3.2.5 on 2022-06-09 16:36

from django.db import migrations, models, transaction
import django.db.models.deletion

# Sender Forward Migration
def user_forwards_func(apps, schema_editor):
    with transaction.atomic():
        db_alias = schema_editor.connection.alias
        user = apps.get_model('api', 'User').objects.using(db_alias)

        with transaction.atomic():
            user.using(db_alias).create(email='andrewsamir2011@gmail.com', username='Andrew Samir', phone='1222963524', address='Farouq Darwish Street', company_name='PyramisaLLC', country='Egypt', city='Alexandria')
            user.using(db_alias).create(email='johngraves@hotmail.com', username='John Graves', phone='3635218971', address='Miami Beach Florida', company_name='FurnLook', country='US', city='Florida')
            user.using(db_alias).create(email='MaxWilson@gmail.com', username='Maxwell Willson', phone='2109547826', address='Via Santo Spirito, Milan', company_name='Giorgio Armani S.p.A.', country='Italy', city='Milano')
            user.using(db_alias).create(email='ahmedyasser123@gmail.com', username='Ahmed Yasser', phone='1115823645', address='Giza, Haram street', company_name='Egypt Air.', country='Egypt', city='Giza')

# Sender Backward Migration
def user_revers_func(apps, schema_editor):
    pass

# Product Forward Migration
def product_forwards_func(apps, schema_editor):
    with transaction.atomic():
        db_alias = schema_editor.connection.alias
        product = apps.get_model('api', 'Product').objects.using(db_alias)

        with transaction.atomic():
            product.using(db_alias).create(name='papers', amount='10000', weight='12.5', origin='Egypt')
            product.using(db_alias).create(name='laptop', amount='1', weight='25', origin='US')
            product.using(db_alias).create(name='air fryer', amount='5', weight='19', origin='France')
            product.using(db_alias).create(name='chargers', amount='50', weight='2.6', origin='Italy')
            product.using(db_alias).create(name='microwave', amount='1', weight='62.5', origin='US')
            product.using(db_alias).create(name='basket balls', amount='500', weight='12', origin='Spain')

# Product Backward Migration
def product_reverse_func(apps, schema_editor):
    pass

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
        migrations.RunPython(user_forwards_func, user_revers_func, atomic=True),
        migrations.RunPython(product_forwards_func, product_reverse_func, atomic=True)
    ]
