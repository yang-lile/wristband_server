from datetime import datetime


def time2stamp(timeString):
    # 企业时间数据转换时间戳
    return int(datetime.strptime(timeString[:19], '%Y-%m-%d %H:%M:%S').timestamp())
