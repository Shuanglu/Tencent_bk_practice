# -*- coding: utf-8 -*-

from django.db import models


class tbl_zhihu(models.Model):
    title = models.TextField()
    link = models.TextField()
    index = models.AutoField(primary_key=True)
class favourite(models.Model):
    num = models.ForeignKey('tbl_zhihu', on_delete=models.CASCADE)
    level = models.IntegerField()

