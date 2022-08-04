import json
from django.db import models

# Create your models here.


class Device(models.Model):
    # 设备基础信息
    conn_time = models.IntegerField(default=0)
    device_id = models.CharField(max_length=15, default='')
    uid = models.CharField(max_length=17, primary_key=True)
    last_res = models.IntegerField(default=0)
    net = models.CharField(max_length=21, default='')
    valid = models.BooleanField(default=False)

    def __str__(self):
        return json.dumps({
            "conn_time": self.conn_time,
            "device_id": self.device_id,
            "uid": self.uid,
            "last_res": self.last_res,
            "net": self.net,
            "valid": self.valid, })


class DeviceInfo(models.Model):

    # 设备具体信息
    timestamp = models.IntegerField(default=0)
    gps = models.BooleanField(default=False)
    # # 维度
    # latitude = models.IntegerField(default=0)
    # # 经度
    # longitude = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    direction = models.IntegerField(default=0)
    altitude = models.IntegerField(default=0)
    satellite_count = models.IntegerField(default=0)
    gsm_signal = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    step = models.IntegerField(default=0)
    turn = models.IntegerField(default=0)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

    # 地理位置信息
    # BSL_count= models.IntegerField(default=0)
    # gms_dely= models.IntegerField(default=0)
    # MCC= models.IntegerField(default=0)
    # MNC= models.IntegerField(default=0)
    # BSLs=models.ExpressionList
    # wifi_count= models.IntegerField(default=0)
    # Wifis=


class DeviceState(models.Model):
    # 设备具体信息中的设备状态
    low_power = models.BooleanField(default=False)
    wear = models.BooleanField(default=False)
    static = models.BooleanField(default=False)
    sos = models.BooleanField(default=False)
    low_power_warn = models.BooleanField(default=False)
    break_warn = models.BooleanField(default=False)
    fall_warn = models.BooleanField(default=False)
    device_info = models.OneToOneField(DeviceInfo, on_delete=models.CASCADE)


class Heartrate(models.Model):
    check_time = models.IntegerField(default=0)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    heart = models.SmallIntegerField(default=0)

class Blood(models.Model):
    check_time = models.IntegerField(default=0)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    systolic_blood = models.PositiveSmallIntegerField(default=0)
    diastolic_blood = models.PositiveSmallIntegerField(default=0)

class OxStart(models.Model):
    check_time = models.IntegerField(default=0)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    oxygen = models.IntegerField(default=0)

class Location(models.Model):
    check_time = models.IntegerField(default=0)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    # 维度
    latitude = models.IntegerField(default=0)
    # 经度
    longitude = models.IntegerField(default=0)