from django.conf.urls import url
from . import views
from blog.logic import template_logic

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^check/$', template_logic.check),
]
