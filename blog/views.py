# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.


def index(request):
    return HttpResponse('This is my blog')


def current_datetime(request):
    now = time.time()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
