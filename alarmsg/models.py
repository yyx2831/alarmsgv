from django.db import models
from sqlserver_ado.fields import BigAutoField
# from django.utils import timezone
from datetime import timedelta, datetime


# Create your models here.
class TbLocid(models.Model):
    locid = models.IntegerField(db_column='locId', primary_key=True)
    locname = models.CharField(db_column='locName', max_length=50, blank=False, null=False)

    class Meta:
        # managed = False
        db_table = 'tb_LocId'


class TbDataaqubool(models.Model):
    id = BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    itemvalue = models.CharField(db_column='itemValue', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    locid = models.ForeignKey(TbLocid, db_column='locId', blank=True, null=True)
    ipaddr = models.CharField(db_column='ipAddr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_DataAquBool'


class TbDataaqufloat(models.Model):
    id = BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    itemvalue = models.CharField(db_column='itemValue', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    locid = models.IntegerField(db_column='locId', blank=True, null=True)  # Field name made lowercase.
    ipaddr = models.CharField(db_column='ipAddr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_DataAquFloat'


class TbDataaquint(models.Model):
    id = BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    itemvalue = models.CharField(db_column='itemValue', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    locid = models.IntegerField(db_column='locId', blank=True, null=True)  # Field name made lowercase.
    ipaddr = models.CharField(db_column='ipAddr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_DataAquInt'


class TbTaggrp(models.Model):
    id = BigAutoField(primary_key=True)
    channelname = models.CharField(db_column='channelName', max_length=30, blank=True,
                                   null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='deviceName', max_length=30, blank=True,
                                  null=True)  # Field name made lowercase.
    updaterate = models.IntegerField(db_column='updateRate', blank=True, null=True)  # Field name made lowercase.
    deadband = models.IntegerField(db_column='deadBand', blank=True, null=True)  # Field name made lowercase.
    activestate = models.NullBooleanField(db_column='activeState')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_TagGrp'


class TbTagid(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=100)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    locid = models.IntegerField(db_column='locId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_TagId'


class TbDataalarm(models.Model):
    id = BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    itemvalue = models.CharField(db_column='itemValue', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    # locid = models.IntegerField(db_column='locId', blank=True, null=True)  # Field name made lowercase.
    locid = models.ForeignKey(TbLocid, db_column='locId', blank=True, null=True)
    ipaddr = models.CharField(db_column='ipAddr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_DataAlarm'

    def was_happened_recent_one_hour(self):
        return self.timestamp >= datetime.now() - timedelta(hours=1)

    def was_happened_recent_one_day(self):
        return self.timestamp >= datetime.now() - timedelta(days=1)

    def was_happened_recent_one_week(self):
        return self.timestamp >= datetime.now() - timedelta(weeks=1)

    def was_happened_recent_one_month(self):
        return self.timestamp >= datetime.now() - timedelta(days=30)


class TbDataaqutime(models.Model):
    id = BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    itemvalue = models.CharField(db_column='itemValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.
    quality = models.CharField(max_length=20, blank=True, null=True)
    locid = models.IntegerField(db_column='locId', blank=True, null=True)  # Field name made lowercase.
    ipaddr = models.CharField(db_column='ipAddr', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'tb_DataAquTime'