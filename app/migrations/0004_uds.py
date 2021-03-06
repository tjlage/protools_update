# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160105_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='UDS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tunnel', models.CharField(blank=True, max_length=4, null=True, verbose_name='Tunnel')),
                ('sysType', models.CharField(blank=True, max_length=4, null=True, verbose_name='System_Type')),
                ('vms', models.CharField(blank=True, max_length=10, null=True, verbose_name='VMS')),
                ('msc', models.CharField(blank=True, max_length=40, null=True, verbose_name='MSC')),
                ('clvstp', models.CharField(blank=True, max_length=5, null=True, verbose_name='CLV_SETUP')),
                ('mscfw', models.CharField(blank=True, max_length=40, null=True, verbose_name='MSC_FW')),
                ('altName', models.CharField(blank=True, max_length=10, null=True, verbose_name='Alternative_Name')),
                ('msc_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='MSC_IP')),
                ('msc_mask', models.GenericIPAddressField(blank=True, null=True, verbose_name='MSC_Mask')),
                ('msc_gate', models.GenericIPAddressField(blank=True, null=True, verbose_name='MSC_Gate')),
                ('msc_sntp', models.GenericIPAddressField(blank=True, null=True, verbose_name='MSC_SNTP')),
                ('sspc_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='SSPC_IP')),
                ('sspc_mask', models.GenericIPAddressField(blank=True, null=True, verbose_name='SSPC_Mask')),
                ('sspc_gate', models.GenericIPAddressField(blank=True, null=True, verbose_name='SSPC_Gate')),
                ('sspc_sntp', models.GenericIPAddressField(blank=True, null=True, verbose_name='SSPC_SNTP')),
            ],
        ),
    ]
