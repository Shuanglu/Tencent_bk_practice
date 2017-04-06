# -*- coding: utf-8 -*-
"""
用于本地开发环境的全局配置
"""
from settings import BASE_DIR
import os

# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',  # 默认用mysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        #'NAME': helloworld,                        # 数据库名 (默认与APP_ID相同)
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'USER': 'root',                        # 你的数据库user
        'PASSWORD': 'shawn~0611',                        # 你的数据库password
        'HOST': '127.0.0.1',                   # 开发的时候，使用localhost
        'PORT': '3306',                        # 默认3306
        'OPTIONS': {
                    'charset': 'utf8',
                    'use_unicode': True, },
    },
}
