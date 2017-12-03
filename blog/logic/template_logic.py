from django.template import Template, Context
from django.http import HttpResponse
__author__ = 'May25th'


def check(request):
    print('check logic')
    html = 'check logic html'
    return HttpResponse(html)
