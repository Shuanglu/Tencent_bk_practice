# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task

from common.log import logger


#@task()
#def async_task(x, y):
#    """
#    定义一个 celery 异步任务
#    """
#    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
#    return x + y
import requests
from bs4 import BeautifulSoup
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

@task()
def async_task():
    smtp_server = 'smtp.qq.com'
    from_user = 'shuanglu1993@foxmail.com'
    from_passwd = 'zjkvnadaofucjbgi'
    to_user = 'shuanglu1993@foxmail.com'

    Msg = MIMEText('bk Django test', 'plain', 'utf-8')
    Msg['From'] = formataddr(['shawn', from_user])
    Msg['To'] = formataddr(['shuang', to_user])
    Msg['Subject'] = 'kindly join the class/辛苦了'

    server = smtplib.SMTP(smtp_server, 25)
    server.starttls()
    server.login(from_user, from_passwd)
    server.sendmail(from_user,to_user,Msg.as_string())
    server.quit()
    print 'sent'




def execute_task_eta():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在xxx后执行，当前时间：{}".format(now))
    # 调用定时任务
    #expected = datetime.datetime(2017, 03, 23, 20, 15, 00)
    expected = datetime.datetime(2017, 03, 23, 04, 05, 00)
    delta = expected - now
    async_task.apply_async(eta=now + delta)


#def execute_task():
#    """
#    执行 celery 异步任务
#
#    调用celery任务方法:
#        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
#        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
#        delay(): 简便方法，类似调用普通函数
#        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
#                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
#    """
#    now = datetime.datetime.now()
#    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
#    # 调用定时任务
#    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


#@periodic_task(run_every=crontab(minute='*/60', hour='*', day_of_week="*"))
#def get_time():
#    """
#    celery 周期任务示例
#
#    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
#    periodic_task：程序运行时自动触发周期任务
#    """
#    execute_task()
#    now = datetime.datetime.now()
#    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))

@periodic_task(run_every=crontab(minute='*/1', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task_period()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))

@task
def execute_task_period():
    conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='shawn~0611', database='test',
                                   use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('USE bkTencent')
    UserAgent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    headers = {'user-agent': UserAgent}
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    print r.encoding

    html = BeautifulSoup(r.content, 'html.parser')
    titles = []
    for title in html.find_all('a'):
        if title.attrs.has_key('class'):
            if title['class'][0] == "question_link":
                titles.append(title.text)

                cursor.execute(
                    'INSERT INTO tbl_zhihu (title, link) VALUES ("{}", "{}")'.format(title.text.encode('utf-8'), title['href'].encode('utf-8')))
                conn.commit()
    cursor.close()

