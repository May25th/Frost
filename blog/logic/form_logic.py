# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
__author__ = 'May25th'


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def ua_display(request):
    # HTTP_USER_AGENT，用户浏览器的user-agent字符串
    # HTTP_REFERER，进站前链接网页
    # REMOTE_ADDR 客户端IP
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s" % ua)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
