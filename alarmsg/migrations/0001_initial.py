# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sqlserver_ado.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbDataalarm',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100, blank=True, null=True, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('itemvalue', models.CharField(max_length=50, blank=True, null=True, db_column='itemValue')),
                ('timestamp', models.DateTimeField(blank=True, null=True, db_column='timeStamp')),
                ('quality', models.CharField(max_length=20, blank=True, null=True)),
                ('ipaddr', models.CharField(max_length=20, blank=True, null=True, db_column='ipAddr')),
            ],
            options={
                'db_table': 'tb_DataAlarm',
            },
        ),
        migrations.CreateModel(
            name='TbDataaqubool',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100, blank=True, null=True, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('itemvalue', models.CharField(max_length=50, blank=True, null=True, db_column='itemValue')),
                ('timestamp', models.DateTimeField(blank=True, null=True, db_column='timeStamp')),
                ('quality', models.CharField(max_length=20, blank=True, null=True)),
                ('ipaddr', models.CharField(max_length=20, blank=True, null=True, db_column='ipAddr')),
            ],
            options={
                'db_table': 'tb_DataAquBool',
            },
        ),
        migrations.CreateModel(
            name='TbDataaqufloat',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100, blank=True, null=True, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('itemvalue', models.CharField(max_length=50, blank=True, null=True, db_column='itemValue')),
                ('timestamp', models.DateTimeField(blank=True, null=True, db_column='timeStamp')),
                ('quality', models.CharField(max_length=20, blank=True, null=True)),
                ('locid', models.IntegerField(blank=True, null=True, db_column='locId')),
                ('ipaddr', models.CharField(max_length=20, blank=True, null=True, db_column='ipAddr')),
            ],
            options={
                'db_table': 'tb_DataAquFloat',
            },
        ),
        migrations.CreateModel(
            name='TbDataaquint',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100, blank=True, null=True, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('itemvalue', models.CharField(max_length=50, blank=True, null=True, db_column='itemValue')),
                ('timestamp', models.DateTimeField(blank=True, null=True, db_column='timeStamp')),
                ('quality', models.CharField(max_length=20, blank=True, null=True)),
                ('locid', models.IntegerField(blank=True, null=True, db_column='locId')),
                ('ipaddr', models.CharField(max_length=20, blank=True, null=True, db_column='ipAddr')),
            ],
            options={
                'db_table': 'tb_DataAquInt',
            },
        ),
        migrations.CreateModel(
            name='TbDataaqutime',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=100, blank=True, null=True, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('itemvalue', models.CharField(max_length=50, blank=True, null=True, db_column='itemValue')),
                ('timestamp', models.DateTimeField(blank=True, null=True, db_column='timeStamp')),
                ('quality', models.CharField(max_length=20, blank=True, null=True)),
                ('locid', models.IntegerField(blank=True, null=True, db_column='locId')),
                ('ipaddr', models.CharField(max_length=20, blank=True, null=True, db_column='ipAddr')),
            ],
            options={
                'db_table': 'tb_DataAquTime',
            },
        ),
        migrations.CreateModel(
            name='TbLocid',
            fields=[
                ('locid', models.IntegerField(primary_key=True, serialize=False, db_column='locId')),
                ('locname', models.CharField(max_length=50, db_column='locName')),
            ],
            options={
                'db_table': 'tb_LocId',
            },
        ),
        migrations.CreateModel(
            name='TbTaggrp',
            fields=[
                ('id', sqlserver_ado.fields.BigAutoField(primary_key=True, serialize=False)),
                ('channelname', models.CharField(max_length=30, blank=True, null=True, db_column='channelName')),
                ('devicename', models.CharField(max_length=30, blank=True, null=True, db_column='deviceName')),
                ('updaterate', models.IntegerField(blank=True, null=True, db_column='updateRate')),
                ('deadband', models.IntegerField(blank=True, null=True, db_column='deadBand')),
                ('activestate', models.NullBooleanField(db_column='activeState')),
            ],
            options={
                'db_table': 'tb_TagGrp',
            },
        ),
        migrations.CreateModel(
            name='TbTagid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('itemname', models.CharField(max_length=100, db_column='itemName')),
                ('itemid', models.IntegerField(blank=True, null=True, db_column='itemId')),
                ('locid', models.IntegerField(blank=True, null=True, db_column='locId')),
            ],
            options={
                'db_table': 'tb_TagId',
            },
        ),
        migrations.AddField(
            model_name='tbdataaqubool',
            name='locid',
            field=models.ForeignKey(blank=True, null=True, db_column='locId', to='alarmsg.TbLocid'),
        ),
        migrations.AddField(
            model_name='tbdataalarm',
            name='locid',
            field=models.ForeignKey(blank=True, null=True, db_column='locId', to='alarmsg.TbLocid'),
        ),
    ]
