from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from httpx import Request
from devices.models import Device, DeviceInfo, DeviceState
from devices.reflesh_server import data_collection
from devices.utils import time2stamp
from devices.models import Blood, Heartrate, OxStart

# Create your views here.


def reflesh(request: Request):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().checkDeviceList()
    if(values == None):
        print('出错')
        return

    jsonData = json.loads(values)
    for device in jsonData['values']:
        deviceModel: Device
        deviceModel = Device(
            conn_time=time2stamp(device['conn_time']),
            device_id=device['device_id'],
            uid=device['id'],
            last_res=time2stamp(device['last_res']),
            net=device['net'],
        )
        deviceModel.save()

        if(device['state'] != None):
            deviceInfo = device['state']
            deviceState = deviceInfo['device_state']
            deviceInfoModel: DeviceInfo = DeviceInfo(
                timestamp=now_time,
                gps=deviceInfo['gps'],
                speed=deviceInfo['speed'],
                direction=deviceInfo['direction'],
                altitude=deviceInfo['altitude'],
                satellite_count=deviceInfo['satellite_count'],
                gsm_signal=deviceInfo['gsm_signal'],
                power=deviceInfo['power'],
                step=deviceInfo['step'],
                turn=deviceInfo['turn'],
                device=deviceModel,
            )
            deviceInfoModel.save()
            deviceStateModel = DeviceState(
                low_power=deviceState['low_power'],
                wear=deviceState['wear'],
                static=deviceState['static'],
                sos=deviceState['sos'],
                low_power_warn=deviceState['low_power_warn'],
                break_warn=deviceState['break_warn'],
                fall_warn=deviceState['fall_warn'],
                device_info=deviceInfoModel,
            )
            deviceStateModel.save()
    jsonData['message'] = '数据正常'
    return JsonResponse(jsonData)


def state(request: Request, uid: str):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().deviceState(uid)
    jsonData = json.loads(values)

    if(values == None or jsonData['values'] == None):
        print('出错')
        return HttpResponse(values)

    deviceInfo = jsonData['values']
    deviceState = deviceInfo['device_state']
    deviceModel = Device.objects.get(uid=uid)
    deviceInfoModel: DeviceInfo = DeviceInfo(
        timestamp=now_time,
        gps=deviceInfo['gps'],
        speed=deviceInfo['speed'],
        direction=deviceInfo['direction'],
        altitude=deviceInfo['altitude'],
        satellite_count=deviceInfo['satellite_count'],
        gsm_signal=deviceInfo['gsm_signal'],
        power=deviceInfo['power'],
        step=deviceInfo['step'],
        turn=deviceInfo['turn'],
        device=deviceModel,
    )
    deviceInfoModel.save()
    deviceStateModel = DeviceState(
        low_power=deviceState['low_power'],
        wear=deviceState['wear'],
        static=deviceState['static'],
        sos=deviceState['sos'],
        low_power_warn=deviceState['low_power_warn'],
        break_warn=deviceState['break_warn'],
        fall_warn=deviceState['fall_warn'],
        device_info=deviceInfoModel,
    )
    deviceStateModel.save()
    
    jsonData['message'] = '数据正常'
    return JsonResponse(jsonData)


def heartrate(request: Request, uid: str):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().deviceHeartRate(uid)
    if(values == None):
        print('出错')
        return

    deviceModel = Device.objects.get(uid=uid)
    jsonData = json.loads(values)
    heartrateModel = Heartrate(
        check_time=now_time,
        device=deviceModel,
        heart=jsonData['values']['heart'],
    )
    heartrateModel.save()
    jsonData['message'] = '数据正常'
    return JsonResponse(jsonData)


def blood(request: Request, uid: str):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().deviceBlood(uid)
    if(values == None):
        print('出错')
        return

    deviceModel = Device.objects.get(uid=uid)
    jsonData = json.loads(values)
    bloodModel = Blood(
        check_time=now_time,
        device=deviceModel,
        systolic_blood=jsonData['values']['Systolic'],
        diastolic_blood=jsonData['values']['Diastolic'],
    )
    bloodModel.save()
    jsonData['message'] = '数据正常'
    return JsonResponse(jsonData)


def oxstart(request: Request, uid: str):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().deviceOxStart(uid)
    if(values == None):
        print('出错')
        return

    deviceModel = Device.objects.get(uid=uid)
    jsonData = json.loads(values)
    oxstartModel = OxStart(
        check_time=now_time,
        device=deviceModel,
        oxygen=jsonData['values']['Oxygen'],
    )
    oxstartModel.save()
    jsonData['message'] = '数据正常'
    return JsonResponse(jsonData)


def location(request: Request, uid: str):
    if(request.method != 'GET'):
        return

    # 当前请求的时间戳
    now_time = int(datetime.now().timestamp())
    values = data_collection().deviceLocation(uid)
    if(values == None):
        print('出错')
        return

    jsonData = json.loads(values)
    pass
