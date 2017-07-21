import win32com.client
from threading import Timer
from django.shortcuts import render_to_response
from . import models
from . import misc_function


# speaker = win32com.client.Dispatch("SAPI.SpVoice")


class acc:
    def __init__(self, s):
        self.s = s

    def inc(self, i):
        if self.s < 3:
            self.s += i
        else:
            self.s = 0
        return self.s


def sound(str):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(str)


def alarm_sound(intv, L=[]):
    # 产生静态增量
    if len(L) == 0:
        L.append(0)
    L[0] += 1
    if L[0] > 4:
        L[0] = 1
    # print(L[0])

    query_res = data_query()
    if len(query_res) > 0:
        msg_single = query_res[L[0] - 1]
        alm_content = msg_single.get('itemname')
        alm_loc = msg_single.get('arrloc')
        alm_cat = msg_single.get('category')
        msg = alm_loc + alm_content + '等级' + alm_cat
        sound(msg)
    t = Timer(intv, alarm_sound, (intv,))
    t.start()
    # print(msg)
    return msg


def data_query():
    alm_count = models.TbDataalarm.objects.all().count()
    if alm_count >= 4:
        bool_data = models.TbDataalarm.objects.order_by('-timestamp')[:4]
        data_list = [{"itemname": item.itemname.split('.')[-1], "category": item.itemvalue,
                      "arrtime": misc_function.dt_utc2nomal(item.timestamp),
                      "arrloc": item.locid.locname} for item in bool_data]
        return data_list
    elif alm_count == 0:
        data_list = [{"itemname": '', "category": '', "arrtime": '', "arrloc": ''}]
        return data_list
    elif alm_count < 4:
        bool_data = models.TbDataalarm.objects.all().order_by('-timestamp')
        data_list = [{"itemname": item.itemname.split('.')[-1], "category": item.itemvalue,
                      "arrtime": misc_function.dt_utc2nomal(item.timestamp),
                      "arrloc": item.locid.locname} for item in bool_data]
        return data_list


def resp_data():
    test_query = [{'itemname': 'first', 'id': 1}, {'itemname': 'second', 'id': 2}]
    return render_to_response('alarmsg/home.html', {'query_res': test_query})
