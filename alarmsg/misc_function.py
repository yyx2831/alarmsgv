# from datetime import timedelta,datetime
import datetime


# 转换为当地时间
def dt_convert2loc(dt):
    dt_res = dt + datetime.timedelta(hours=8)
    return dt_res


def dt_utc2nomal(dt):
    # dt_res = dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    LOCAL_FORMAT = '%Y-%m-%d %H:%M:%S'
    # LOCAL_FORMAT = '%Y-%m-%d%H:%M'
    dt_temp = dt + datetime.timedelta(hours=8)
    # dt_fmt=datetime.datetime.(dt_temp,LOCAL_FORMAT)
    # dt_res.strftime('%b-%d-%y %H:%M:%S')
    # a = str(dt_res)
    # i = a.split("T")
    # a = a[:i]+a[i:]
    # i = a.split("Z")
    # a = a[:i]
    # dt_res = datetime.datetime.strptime(a, '%b-%d-%y %H:%M')
    # dt_res = datetime.datetime.utcfromtimestamp(dt) + datetime.timedelta(hours=8)
    dt_str = str(dt_temp).split('+')[0]
    dt_res = datetime.datetime.strptime(dt_str, LOCAL_FORMAT)
    return dt_res
