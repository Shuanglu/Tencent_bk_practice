# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.views.decorators.csrf import csrf_exempt
from .views import fav, rem
#urlpatterns = patterns('home_application.views',
#    (r'^$', 'home'),
#    (r'^dev-guide/$', 'dev_guide'),
#    (r'^contactus/$', 'contactus'),
#)

app_name = 'home_application'
urlpatterns = patterns('',
    (r'^$', 'home_application.views.index'),
    (r'^option$', 'home_application.views.option'),
    (r'^upload$', 'home_application.views.upload'),
    (r'^func$', 'home_application.views.func'),
    (r'^search$', 'home_application.views.search'),
    (r'^refresh$', 'home_application.views.refresh'),
    (r'^fav$', csrf_exempt(fav) ),
    (r'^rem$', csrf_exempt(rem) ),
)