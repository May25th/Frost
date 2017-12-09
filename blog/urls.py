from django.conf.urls import url
from . import views
from blog.logic import template_logic
from blog.logic import book_logic
from blog.logic import form_logic

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^check/$', template_logic.check),
    url(r'^test_template/$', template_logic.test_template),
    url(r'^add_book/$', book_logic.add_book),
    url(r'^get_book_list/$', book_logic.get_book_list),
    url(r'^current_url_view_good/$', form_logic.current_url_view_good),
    url(r'^ua_display/$', form_logic.ua_display),
    url(r'^display_meta/$', form_logic.display_meta),
]
