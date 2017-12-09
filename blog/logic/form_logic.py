# -*- coding: utf-8 -*-
from django.http import HttpResponse
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
