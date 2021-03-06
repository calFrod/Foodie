# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('nric', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('hp_no', models.CharField(max_length=8)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_particulars',
            fields=[
                ('stall_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('stall_name', models.CharField(max_length=100)),
                ('block_no', models.CharField(max_length=10, null=True)),
                ('street_no', models.CharField(max_length=50)),
                ('stall_no', models.CharField(max_length=10)),
                ('postal_cd', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=50)),
                ('start_operation_time', models.CharField(max_length=5)),
                ('end_operation_time', models.CharField(max_length=5)),
                ('operation_days', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=500, null=True)),
                ('nric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Owner', verbose_name='Stall Owner IC')),
            ],
        ),
    ]
