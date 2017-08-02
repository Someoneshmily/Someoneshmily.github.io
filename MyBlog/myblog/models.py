# coding=utf-8
from django.db import models

# Create your models here.


class PersonInfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=40)  # sha1
    email = models.CharField(max_length=30)
    address = models.CharField(default='', max_length=100)  # 地址
    code = models.CharField(default='', max_length=6)  # 编码
    phone = models.CharField(default='', max_length=11)  # 机号

class BlogContent(models.Model):
    title = models.CharField('标题', max_length=31)
    # 摘要
    summray = models.TextField('摘要')
    # 内容
    content = models.TextField('内容')
    # 　创建时间
    # 当blogmodel对象第一次创建时，自动把时间传入并且不再更改
    createdTime = models.DateTimeField('创建时间', auto_now_add=True)
    # 　上次更新时间
    # 当模型对象实力调用save方法时会把当前时间传入
    editTime = models.DateTimeField('最近更新时间', auto_now=True)
    # 分类
    category = models.CharField('分类', max_length=31)
    category_num = models.IntegerField('类别编号',default=0)
    # 访问量
    vistedNumber = models.IntegerField('访问量', default=0)
    # 关键词
    keywords = models.CharField('关键词', max_length=63)


class Mesage(models.Model):
    #　留言
    leave_msg = models.TextField('内容')
    createdTime = models.DateTimeField('创建时间', auto_now_add=True)
    # 　上次更新时间
    # 当模型对象实力调用save方法时会把当前时间传入
    editTime = models.DateTimeField('最近更新时间', auto_now=True)
