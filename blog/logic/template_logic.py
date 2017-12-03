from django.template import Template, Context
from django.http import HttpResponse
__author__ = 'May25th'


def check(request):
    t = Template('My name is {{ name }}.')
    c = Context({'name': 'May25th'})
    html = t.render(c)
    return HttpResponse(html)
