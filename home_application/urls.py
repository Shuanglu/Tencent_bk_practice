# -*- coding: utf-8 -*-

from django.conf.urls import patterns


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
)