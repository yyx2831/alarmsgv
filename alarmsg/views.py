from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder
import json
from . import models
from . import scheduled_job
from . import misc_function
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from django import forms
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from alarmsg.app_forms import UserForm, LocForm
from django.contrib import auth
from datetime import timedelta, datetime


@csrf_protect
def login(request):
    # if request.method == 'GET':  # 页面初次显示
    #     form = app_forms.UserForm()
    #     return render_to_response('alarmsg/login.html', RequestContext(request, {'form': form}))
    # else:
    #     form = app_forms.UserForm(request.POST)  # 页面提交数据
    #     if form.is_valid():
    #         uname = form.cleaned_data['username']
    #         pword = form.cleaned_data['password']
    #         # user = TbUser.objects.filter(username__exact=username, password__exact=password)
    #         # user = TbUser.objects.filter(username=username, password=password)
    #         user = authenticate(username=uname, password=pword)
    #         if user:
    #             return render_to_response('alarmsg/home.html', {'userform': form},
    #                                       context_instance=RequestContext(request))
    #         else:
    #             # return HttpResponse('用户名或密码错误,请重新登录')
    #             return render_to_response('alarmsg/login.html', {'userform': form, 'password_is_wrong': True},
    #                                       context_instance=RequestContext(request))
    #     else:
    #         return render_to_response('alarmsg/login.html',
    #                                   RequestContext(request, {'form': form}))  # 如果页面数据提交有问题，刷新页面
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            # user = User.objects.filter(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                # if user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect('/alarmsg/home', {'userform': userform, 'username': username})
                # return HttpResponseRedirect('/alarmsg/home', {'username': user.username})
                return HttpResponseRedirect('/alarmsg/home/?user=' + user.username)

            else:
                # return HttpResponse('用户名或密码错误,请重新登录')
                return render_to_response('alarmsg/login.html', {'userform': userform},
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('alarmsg/login.html', context_instance=RequestContext(request))
    else:
        userform = UserForm()
        # return render_to_response('alarmsg/login.html', RequestContext(request, {'userform': userform}))
        return render_to_response('alarmsg/login.html', {'userform': userform},
                                  context_instance=RequestContext(request))


# @login_required
def logout_view(request):
    auth.logout(request)
    userform = UserForm()
    # return render_to_response('alarmsg/login.html', {'userform': userform}, context_instance=RequestContext(request))
    # return HttpResponseRedirect('/alarmsg/login')
    return HttpResponseRedirect('/')


# TODO: 数据查询测试
def test(request):
    bool_data = models.TbDataaqubool.objects.order_by('-timestamp')[:4]
    msg_arr = bool_data.values('itemname', 'itemvalue', 'timestamp', 'locid')
    msg = scheduled_job.alarm_sound(msg_arr, 2)
    return render(request, 'alarmsg/test.html')


def fetch_recent(request):
    bool_data = models.TbDataalarm.objects.order_by('-timestamp')[:4]
    data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue,
                  "arrtime": misc_function.dt_utc2nomal(item.timestamp),
                  "arrloc": item.locid.locname} for item in bool_data]
    sum_danger = models.TbDataalarm.objects.filter(itemvalue='严重').count()
    sum_warning = models.TbDataalarm.objects.filter(itemvalue='一般').count()
    sum_light = models.TbDataalarm.objects.filter(itemvalue='轻微').count()
    return JsonResponse(
        {'msg_fetch': data_list, 'sum_danger': sum_danger, 'sum_warning': sum_warning, 'sum_light': sum_light})


@login_required
def home(request):
    current_msg = scheduled_job.alarm_sound(2)
    scheduled_job.resp_data()
    username = request.GET.get('user', '')
    return render(request, 'alarmsg/home.html', {'msg': current_msg, 'username': username, 'show_cur_alm': True})


# ajax临时测试部分
def data(request, id):
    rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
    rlist2 = []
    rlist2.append({"name": rlist[int(id)][0], "subject": rlist[int(id)][1]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response


def update(request):
    return render_to_response('alarmsg/update.html')


def set_list(msg_arr):
    list_result = []
    for obj in msg_arr:
        m0 = obj.get('itemname')
        m1 = obj.get('itemvalue')
        m2 = obj.get('timestamp')
        m3 = obj.get('locid')
        mjh = {'itemname': '', 'itemvalue': '', 'timestamp': '', 'locid': ''}
        m4 = m0.split('.')[-1]
        mjh['itemname'] = m4
        mjh['itemvalue'] = m1
        mjh['timestamp'] = m2
        mjh['locid'] = m3
        # print(mjh)
        list_result.append(mjh)
    return list_result


def add1(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# @login_required
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


@login_required
def subworks(request, loc):
    # TODO 分厂地址字典，需与URL吻合
    locname_dic = {'1': '一分厂', '2': '二分厂', '3': '三分厂', '5': '锅炉房', '97': '文山分厂', '68': '水富分厂', '4': '硝铵集中溶化'}
    default_name = '空值'
    real_name = locname_dic.get(loc, default_name)
    bool_data = models.TbDataalarm.objects.filter(locid__locname=real_name).order_by('-timestamp')[:4]
    data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue,
                  "arrtime": misc_function.dt_convert2loc(item.timestamp),
                  "arrloc": item.locid.locname} for item in bool_data]
    return render_to_response('alarmsg/subworks.html',
                              {'locmsg': data_list, 'locid': real_name, 'show_cur_alm': True})


@login_required
def categories(request, cat):
    category_dic = {'danger': '严重', 'normal': '一般', 'light': '轻微'}
    default_name = '未定义'
    category_name = category_dic.get(cat, default_name)
    bool_data = models.TbDataalarm.objects.filter(itemvalue=category_name).order_by('-timestamp')
    data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
                  "arrloc": item.locid.locname} for item in bool_data]
    return render_to_response('alarmsg/categroies.html', {'catmsg': data_list, 'cat': cat, 'show_cur_alm': False})


@login_required
def summary(request):
    # category_dic = {'danger': '严重', 'normal': '一般', 'light': '轻微'}
    # default_name = '未定义'
    # category_name = category_dic.get(cat, default_name)
    bool_data_danger = models.TbDataalarm.objects.filter(itemvalue='严重').order_by('-timestamp')
    data_list_danger = [
        {"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
         "arrloc": item.locid.locname} for item in bool_data_danger]

    bool_data_normal = models.TbDataalarm.objects.filter(itemvalue='一般').order_by('-timestamp')
    data_list_normal = [
        {"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
         "arrloc": item.locid.locname} for item in bool_data_normal]

    bool_data_light = models.TbDataalarm.objects.filter(itemvalue='轻微').order_by('-timestamp')
    data_list_light = [
        {"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
         "arrloc": item.locid.locname} for item in bool_data_light]

    danger_msg = bool_data_danger.count()
    normal_msg = bool_data_normal.count()
    light_msg = bool_data_light.count()

    return render_to_response('alarmsg/summary.html', {'danger_msg': danger_msg, 'normal_msg': normal_msg,
                                                       'light_msg': light_msg, 'show_cur_alm': False})


@login_required
def setup(request):
    loc_queryset = models.TbLocid.objects.all().order_by('locid')
    # loc_list = [{'locid': item.locid, 'locname': item.locname} for item in loc_queryset]
    # return render_to_response('alarmsg/setup.html', {'loc_list': loc_list, 'show_cur_alm': False})
    return render_to_response('alarmsg/setup.html',
                              {'locs': loc_queryset, 'show_cur_alm': False, 'show_edit': False, 'show_add': False,
                               'show_del': False})


@login_required
@csrf_protect
def loc_edit(request, locid):
    loc_queryset = models.TbLocid.objects.all().order_by('locid')
    if request.method == 'GET':
        # loc_queryset = models.TbLocid.objects.all().order_by('locid')
        loc_msg = models.TbLocid.objects.filter(locid__exact=locid)
        form = LocForm()
        # form.id = locid
        # form.name = loc_msg.values('locname')[0]
        # title_text = '编辑'
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'details': loc_msg, 'loc_form': form, 'show_cur_alm': False,
                                   'show_edit': True, 'show_add': False}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        # print('in POST')
        form = LocForm(request.POST)
        if form.is_valid():
            # print('form is valid')
            l_id = form.cleaned_data['id']
            l_name = form.cleaned_data['name']
            # if locid == 1000:  # 编辑
            obj = models.TbLocid.objects.get(locid=l_id)
            obj.locname = l_name
            obj.save()
            # elif locid == 1001:  # 增加
            #     models.TbLocid.objects.create(locid=l_id, locname=l_name)
            return render_to_response('alarmsg/setup.html',
                                      {'locs': loc_queryset, 'show_cur_alm': False, 'show_edit': False,
                                       'show_add': False,
                                       'loc_form': form},
                                      context_instance=RequestContext(request))
    else:
        print('form is invalid')
        form = LocForm()
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'show_cur_alm': False, 'show_edit': True, 'show_add': False,
                                   'loc_form': form},
                                  context_instance=RequestContext(request))


@login_required
@csrf_protect
def loc_add(request):
    loc_queryset = models.TbLocid.objects.all().order_by('locid')
    if request.method == 'GET':
        # loc_msg = models.TbLocid.objects.filter(locid__exact=locid)
        form = LocForm()
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'loc_form': form, 'show_cur_alm': False,
                                   'show_edit': False, 'show_add': True}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = LocForm(request.POST)
        if form.is_valid():
            l_id = form.cleaned_data['id']
            l_name = form.cleaned_data['name']
            models.TbLocid.objects.create(locid=l_id, locname=l_name)
            return render_to_response('alarmsg/setup.html',
                                      {'locs': loc_queryset, 'show_cur_alm': False, 'show_edit': False,
                                       'show_add': False,
                                       'loc_form': form},
                                      context_instance=RequestContext(request))
        else:
            print('form is invalid')
            return render_to_response('alarmsg/setup.html',
                                      {'locs': loc_queryset, 'show_cur_alm': False, 'show_edit': True,
                                       'show_add': False,
                                       'loc_form': form},
                                      context_instance=RequestContext(request))


@login_required
@csrf_protect
def loc_del(request, locid, action):
    # loc_queryset = models.TbLocid.objects.all().order_by('locid')
    if action == 'y':
        # loc_msg = models.TbLocid.objects.filter(locid__exact=locid)
        models.TbLocid.objects.filter(locid=locid).delete()
        loc_queryset = models.TbLocid.objects.all().order_by('locid')
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'show_cur_alm': False,
                                   'show_edit': False, 'show_add': False, 'show_del': False},
                                  )
    elif action == 'n':
        # loc_msg = models.TbLocid.objects.filter(locid__exact=locid)
        # models.TbLocid.objects.filter(locid=locid).delete()
        loc_queryset = models.TbLocid.objects.all().order_by('locid')
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'show_cur_alm': False,
                                   'show_edit': False, 'show_add': False, 'show_del': False},
                                  )
    elif action == 'c':
        loc_queryset = models.TbLocid.objects.all().order_by('locid')
        loc_msg = models.TbLocid.objects.filter(locid__exact=locid)
        l_id = locid
        l_name = models.TbLocid.objects.get(locid=l_id).locname
        return render_to_response('alarmsg/setup.html',
                                  {'locs': loc_queryset, 'details': loc_msg, 'locid': l_id, 'locname': l_name,
                                   'show_cur_alm': False, 'show_edit': False,
                                   'show_add': False,
                                   'show_del': True},
                                  )


@login_required
def query_view(request):
    loc_queryset = models.TbLocid.objects.all().order_by('locid')
    loc_list = [{'locid': item.locid, 'locname': item.locname} for item in loc_queryset]
    rec_list = ['过去一小时', '过去一天', '过去一周', '过去一月']
    cat_list = ['严重', '一般', '轻微']
    return render_to_response('alarmsg/query.html',
                              {'loc_list': loc_list, 'rec_list': rec_list, 'cat_list': cat_list, 'show_cur_alm': False,
                               'show_edit': False, 'show_add': False, 'show_del': False})


# @csrf_protect
@login_required
def query_start(request, loc, rec, cat):
    # rec_dic = {'1': '过去一小时', '2': '过去一天', '3': '过去一周', '4': '过去一月'}
    cat_dic = {'1': '严重', '2': '一般', '3': '轻微'}
    default_name = ' '
    # rec_name = rec_dic.get(rec, default_name)
    cat_name = cat_dic.get(cat, default_name)
    # bool_data_raw = models.TbDataalarm.objects.filter(locid=loc, itemvalue=cat_name).order_by('-timestamp')[:20]
    if rec == '1':  # 过去一小时
        start = datetime.now() - timedelta(hours=1)
        bool_data = models.TbDataalarm.objects.filter(locid=loc, itemvalue=cat_name,
                                                      timestamp__range=(start, datetime.now())).order_by('-timestamp')[
                    :20]
        data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
                      "arrloc": item.locid.locname} for item in bool_data]
        return JsonResponse({'result': data_list})
    if rec == '2':  # 过去一天
        start = datetime.now() - timedelta(days=1)
        bool_data = models.TbDataalarm.objects.filter(locid=loc, itemvalue=cat_name,
                                                      timestamp__range=(start, datetime.now())).order_by('-timestamp')[
                    :20]
        data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
                      "arrloc": item.locid.locname} for item in bool_data]
        return JsonResponse({'result': data_list})
    if rec == '3':  # 过去一周
        start = datetime.now() - timedelta(weeks=1)
        bool_data = models.TbDataalarm.objects.filter(locid=loc, itemvalue=cat_name,
                                                      timestamp__range=(start, datetime.now())).order_by('-timestamp')[
                    :20]
        data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
                      "arrloc": item.locid.locname} for item in bool_data]
        return JsonResponse({'result': data_list})
    if rec == '4':  # 过去一月
        start = datetime.now() - timedelta(days=30)
        bool_data = models.TbDataalarm.objects.filter(locid=loc, itemvalue=cat_name,
                                                      timestamp__range=(start, datetime.now())).order_by('-timestamp')[
                    :20]
        data_list = [{"itemname": item.itemname.split('.')[-1], "itemvalue": item.itemvalue, "arrtime": item.timestamp,
                      "arrloc": item.locid.locname} for item in bool_data]
        return JsonResponse({'result': data_list})
    return JsonResponse({'result': []})
