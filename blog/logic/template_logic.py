# -*- coding: utf-8 -*-
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.conf import settings
__author__ = 'May25th'


def check(request):
    t = Template('My name is {{ name }}.')
    c = Context({'name': 'May25th'})
    html = t.render(c)
    return HttpResponse(html)


def test_template_old(request):
    fp = open(settings.BLOG_TEMPLATE_DIR + 'test.html')
    t = get_template(fp.read())
    fp.close()
    html = t.render(Context({'mark': 'BMW'}))
    return HttpResponse(html)


def test_template_old2(request):
    t = get_template('moban.html')
    # 版本不一样 语法不一样
    html = t.render({'mark': 'BMW'})
    return HttpResponse(html)


def test_template(request):
    # 更简单的实现
    return render_to_response('moban.html', {'mark': 'Too Young'})
