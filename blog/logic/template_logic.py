from django.template import Template, Context
from django.http import HttpResponse
from django.conf import settings
__author__ = 'May25th'


def check(request):
    t = Template('My name is {{ name }}.')
    c = Context({'name': 'May25th'})
    html = t.render(c)
    return HttpResponse(html)


def test_template(request):
    fp = open(settings.BLOG_TEMPLATE_DIR + 'test.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'mark': 'BMW'}))
    return HttpResponse(html)
