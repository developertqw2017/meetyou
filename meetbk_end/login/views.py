from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .checkuser import checkdata
import requests

# Create your views here.
def test(request):
    return JsonResponse({'data':'info'})

#处理登录
@csrf_exempt
def verify_user(request):
    if request.method == "POST":
        #print(request.POST)
        #初始化返回的字典
        data = {}

        #获取小程序数据
        code = request.POST.get('code')
        encrypteddata = request.POST.get('encrypteddata')
        iv = request.POST.get('iv')

        #检查用户
        res = checkdata(code, encrypteddata, iv)
        #print('解码信息',res)
        #检查不通过
        errorinfo = res.get('error',None)
        if errorinfo:
            return JsonResponse(res)

        openid = res['openid']

        user = authenticate(username=openid,password=openid)
        #登录用户并保存cookie
        if user:
            login(request, user)
            query_user = Profile.objects.get(openid=openid)
            query_user.cookie = res['cookie']
            query_user.save()

            #获取用户发送的信件
            data['status'] = '已登录'
        #新建用户
        else:
            user_ins = User.object.create_user(
                username=openid,
                password=openid
            )
            profile = Profile.objects.create(
                user=user_ins,
                openid=openid,
                cookie=res['cookie'],
                nickname=res['nickName'],
                gender=res['gender']
            )
            new_user = authenticate(username=openid, password=openid)
            login(request, new_user)
            data['dirs'] = ['默认']
            data['status'] = '已创建并登录'

        data['info'] = res
        #print('最终返回信息', data)

        return JsonResponse(data)
    data = {'error':'仅接受POST请求'}
    return JsonResponse(data)
