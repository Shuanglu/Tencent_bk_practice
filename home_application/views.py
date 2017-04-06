# -*- coding: utf-8 -*-
# encoding=utf-8
#from common.mymako import render_mako_context
from django.http import HttpResponse
from django.shortcuts import render
import os
import hashlib
import requests
from bs4 import BeautifulSoup
import mysql.connector
from .models import tbl_zhihu, favourite
from django.core import serializers
import json
from django.forms.models import model_to_dict
import simplejson
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    """
    首页
    """
#    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
#    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
#    return render_mako_context(request, '/home_application/contact.html')


def index(request):
    #return HttpResponse('hello blueking')
    from celery_tasks import execute_task_eta
    #execute_task_eta()
    return render(request, 'home_application/index.html')

def option(request):
    return HttpResponse('congratulation!')


def upload(request):
    #assert False
    if request.method == 'POST':
        if request.FILES['file']:
            file = request.FILES['file']
            #print request.FILES['file']
            with open(os.path.join("/home/shawn/", file.name), 'wb+') as f:
                print os.path.join("/home/shawn/", file.name)
                for chunk in file.chunks():
                        f.write(chunk)
            with open(os.path.join("/home/shawn/", file.name), 'rb') as f:
                myhash = hashlib.md5()
                print myhash.hexdigest()
                while True:
                    b = f.read(8096)
                    if not b:
                        break
                    myhash.update(b)
                print myhash.hexdigest()
            os.remove(os.path.join("/home/shawn/", file.name))
            print myhash.hexdigest()
            return HttpResponse(myhash.hexdigest())
        else:
            return HttpResponse('Failed')




def search(request):
    searchTitle = unicode(request.GET['title'])
    print searchTitle
    conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='shawn~0611', database='test',
                                   use_unicode=True, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('USE test')
    cursor.execute(
        'SELECT * FROM home_application_tbl_zhihu WHERE title LIKE "%{}%"'.format(searchTitle.encode('utf-8'))
    )
    res = cursor.fetchall()
    for items in res:
        print [unicode(item).encode('utf-8') for item in items]
    cursor.close()
    return HttpResponse(len(res))




def refresh(request):
    conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='shawn~0611', database='test',
                                   use_unicode=True, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('USE test')
    cursor.execute(
        'DELETE FROM home_application_tbl_zhihu'
    )
    UserAgent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    headers = {'user-agent': UserAgent}
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    print r.encoding

    html = BeautifulSoup(r.content, 'html.parser')
    titles = []
    index = 0
    for title in html.find_all('a'):

        if title.attrs.has_key('class'):
            if title['class'][0] == "question_link":
                titles.append(title.text)
                #print title.text
                cursor.execute(
                    'INSERT INTO home_application_tbl_zhihu (title, link) VALUES ("{}", "{}")'.format(title.text.encode('utf8'), title['href']))
                conn.commit()
                cursor.execute(
                    'DELETE FROM home_application_favourite'
                )
                conn.commit()
#                cursor.execute(
#                    'SELECT * FROM tbl_zhihu'
#                )
#                for row in cursor.fetchall():
#                    print len(row)
#                    print row[0]
#                    print row[1]
#                conn.commit()
    cursor.close()
#    Topics = json.dumps(model_to_dict(tbl_zhihu.objects.all()))
#    Topics = simplejson.dumps(tbl_zhihu.objects.all(), encoding='utf-8', ensure_ascii=False)
#    Topics = simplejson.dumps({'row': [model_to_dict(item) for item in tbl_zhihu.objects.all()]}, ensure_ascii=False, encoding='utf-8')
#    data = {'a': u'的'}
#    print [unicode(item.__dict__) for item in tbl_zhihu.objects.all()]
#    print tbl_zhihu.objects.values_list('title')
#    Topics = unicode(tbl_zhihu.objects.all().__dict__)
#    print model_to_dict()
    #    for key in data.keys():
#        data[key] = unicode(data[key])
#    Topics = simplejson.dumps(data,ensure_ascii=False)
#    print tbl_zhihu.objects.all()
    Topics = serializers.serialize('json', tbl_zhihu.objects.all(), ensure_ascii=False)
    topic = tbl_zhihu.objects.filter(index=4)
    print serializers.serialize('json', topic)
#    print tbl_zhihu.objects.all()
#    Topics = json.dumps(tbl_zhihu.objects.all(), ensure_ascii=False, encoding='utf-8')
    #print Topics

    return HttpResponse(Topics, content_type="application/json", charset='utf-8')

def func(request):
    return render(request, 'home_application/func.html')



def fav(request):
    id = int(request.POST['pk'])
#    print id
    level = request.POST['level']
#    print tbl_zhihu.objects.get(index=1)
#    print tbl_zhihu.objects.filter(index=id)
#    print favourite.objects.filter(num=tbl_zhihu.objects.get(index=id))
#    favourite.objects.get(num=tbl_zhihu.objects.get(index=id))
#    favourite.objects.update_or_create()
    try:
        favourite.objects.get(num=tbl_zhihu.objects.get(index=id))
    except ObjectDoesNotExist, e:
#        print e
        favourite.objects.create(num=tbl_zhihu.objects.get(index=id), level=level)
    else:
        favourite.objects.filter(num=tbl_zhihu.objects.get(index=id)).update(level=level)
    return HttpResponse('success')


def rem(request):
    id = int(request.POST['pk'])
    print id
#    print tbl_zhihu.objects.get(index=1)
#    print tbl_zhihu.objects.filter(index=id)
#    print favourite.objects.filter(num=tbl_zhihu.objects.get(index=id))
#    favourite.objects.get(num=tbl_zhihu.objects.get(index=id))
#    try:
#        favourite.objects.get(num=tbl_zhihu.objects.get(index=id))
#    except ObjectDoesNotExist, e:
#        print e
#        favourite.objects.create(num=tbl_zhihu.objects.get(index=id), level=level)
#    else:
#        favourite.objects.filter(num=tbl_zhihu.objects.get(index=id)).update(level=level)
    favourite.objects.filter(num=tbl_zhihu.objects.get(index=id)).delete()
    print favourite.objects.filter(num=tbl_zhihu.objects.get(index=id))
    return HttpResponse('success')


