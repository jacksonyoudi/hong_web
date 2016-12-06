# coding: utf8
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
import json
from web import models
from web import common
from django.utils.safestring import mark_safe
from myweb.common import html_page
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


def ajax(request):
    if request.method == 'POST':
        print request.POST
        data = {'status': 0, 'msg': '请求成功', 'data': [11, 22, 33, 44]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('ajax.html')


def index(request, *args, **kwargs):
    print args
    print kwargs
    page = kwargs['page']
    per_item = int(request.COOKIES.get('pager_num', 10))
    try:
        page = int(page)  # 当前页
    except Exception, e:
        page = 1
    # 第一页是 0 到 5 (page-1)*5 ---(page*5)
    # 第2页是 5 到 10 (page-1)*5 ---(page*5)
    count = models.Host.objects.all().count()

    # count
    # page_item 默认值 5
    # page

    pageobj = html_page.PageInfo(page, count, per_item)
    # start
    # end
    # all_page_count

    result = models.Host.objects.all()[pageobj.start:pageobj.end]
    count = models.Host.objects.all()[pageobj.start:pageobj.end].count()

    page_html = html_page.Pager(page, pageobj.all_page_count)
    ret = {'data': result, 'count': count, 'page': page_html}
    response = render_to_response('index.html', ret)
    response.set_cookie('pager_num', per_item)
    return response


def add(request):
    for i in xrange(100, 200):
        hostname = 'hostname' + str(i)
        ip = '192.168.1.' + str(i)
        models.Host.objects.create(HostName=hostname, IP=ip)

    return HttpResponse('ok')


def ipmap(request):
    return render_to_response('ip.html')


@api_view(['GET', 'PUT', 'POST'])
def server(request):
    method = request.method
    if method == 'POST':
        pass
    return Response('aaabbbb')


from PIL import Image, ImageFont, ImageDraw
from random import randint


def verify(request, width, height):
    wordsCount = 4  # 验证码中的字符个数
    width = int(width)  # 图片宽度
    # 字体大小的设置
    size = int(min(width / wordsCount, height / 1.5))
    # 随机背景颜色
    bgColor = (randint(200, 255), randint(200, 255), randint(200, 255))
    # 创建图像
    img = Image.new('RGB', (width, height), bgColor)
    # 导入字体
    font = ImageFont.truetype('Arial.ttf', size)
    # 创建画笔
    draw = ImageDraw.Draw(img)

    # 导入StringIO模块
    from StringIO import StringIO
    # 建立一个缓存对象
    mstream = StringIO
    # 将图片保存到内存中
    img.save(mstream, 'jpeg')
    # 返回内存中的图片
    return HttpResponse(mstream.getvalue(), 'image/jpeg')

