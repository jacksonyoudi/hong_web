#!/usr/bin/env python
# coding: utf8

from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username == 'youdi' and password == '123':
            request.session['is_login'] = True  # 登录成功后，在session的字典中设置k-v值，用于标记登录状态
            return redirect('/study/index')
        else:
            return render_to_response('study/login.html', {'msg': '用户名或密码错误！'})
    else:
        return render_to_response('study/login.html', {'msg': ''}, context_instance=RequestContext(request))


def index(request):
    is_login = request.session.get('is_login', None)  # 获取登录状态
    if not is_login:
        return redirect('/study/login/')
    else:
        return render_to_response('study/index.html')

# def login(request):
#     del request.session['is_login']  # 销毁session
#     return redirect('/study/login')
