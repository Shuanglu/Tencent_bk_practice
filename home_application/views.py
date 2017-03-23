# -*- coding: utf-8 -*-

#from common.mymako import render_mako_context
from django.http import HttpResponse
from django.shortcuts import render
import os
import hashlib

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