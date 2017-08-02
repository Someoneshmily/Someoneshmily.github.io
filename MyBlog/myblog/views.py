# coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse,HttpResponse
from django.db import transaction
# Create your views here.

def index(request):
    exist='0'
    content_list = BlogContent.objects.all()
    if len(content_list) <= 0:
        exist = '1'

    context = {"content_list":content_list,"exist":exist}
    return render(request, 'myblog/index.html',context)


def formdata(request):
    return render(request, 'myblog/formdata.html')



def edit_html(request,id):
    obj = BlogContent.objects.get(pk=id)
    context = {"obj":obj}
    return render(request, 'myblog/edit.html',context)


def data(request):
    return render(request, 'myblog/blog.json')


# 增
def create(request):
    # 创建博客对象
    blog = BlogContent()
    # 获取ｈｔｍｌ页面数据
    title = request.GET.get('title')
    summray = request.GET.get('summray')
    content = request.GET.get('content')
    category = request.GET.get('category')
    keywords = request.GET.get('keywords')
    category_num = request.GET.get('val')

    blog.title = title
    blog.summray = summray
    blog.content = content
    blog.category = category
    blog.keywords = keywords
    blog.category_num = int(category_num)
    blog.save()

    return JsonResponse({"isadd":1})


# 删
def delete(request):
    id = int(request.GET.get('id'))
    obj = BlogContent.objects.get(pk=id)
    obj.delete()

    return JsonResponse({"isdel":1})


# 查
def findAll(request):
    all_info = BlogContent.objects.all()
    context = {'content_list':all_info}
    return render(request,'myblog/findAll.html',context)

#
# def findOne(request, id):
#     pass
#     one = BlogContent.objects.get(pk=id)
#     context = {'one':one}
#     return render(request,'myblog/find.html',context)


def edit(request):
    # 获取页面信息，兵且在编辑条框内显示已经存在的信息，当点击提交的时候，对数据库进行更改保存，当前信息重新从数据库进行读取，并显示
    id = int(request.GET.get('id'))
    obj = BlogContent.objects.get(pk=id)
    title = request.GET.get('title')
    summray = request.GET.get('summray')
    content = request.GET.get('content')
    category = request.GET.get('category')
    keywords = request.GET.get('keywords')

    obj.title = title
    obj.summray = summray
    obj.content = content
    obj.category = category
    obj.keywords = keywords
    obj.save()

    return JsonResponse({'ok':1})

# 留言区
def leave_msg(request):
    leninfo = '0'
    all_info = Mesage.objects.all()
    if len(all_info) <= 0:
        leninfo = '1'
    context = {'content_list': all_info,'msg':'1','leninfo':leninfo}
    return render(request,'myblog/leave_msg.html',context)

def msg_data(request):
    return render(request,'myblog/msg_data.html')

def create_msg(request):
    msg = Mesage()
    # 获取ｈｔｍｌ页面数据
    content = request.GET.get('content')
    msg.leave_msg = content
    msg.save()

    return JsonResponse({"ok": 1})










