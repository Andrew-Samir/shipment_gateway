# Generated by Django 3.2.5 on 2022-06-09 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
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
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.courier')),
            ],
            options={
                'db_table': 'courier',
            },
        ),
    ]