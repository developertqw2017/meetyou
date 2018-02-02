from django.shortcuts import render
from django.http import JsonResponse
from .model import *
from django.core import serializers
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from . cheuser import checkdata
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

        openid = res['openId']

        user = authenticate(username=openid,password=openid)
        #登录用户并保存cookie
        if user:
            login(request, user)
            query_user = Profile.objects.get(openid=openid)
            query_user.cookie = res['cookie']
            query_user.save()


