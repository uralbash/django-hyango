# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from views import PageView

urlpatterns = patterns('',
                       url(r'^(?P<url>.*?)/$', PageView.as_view(),
                           name="page"),
                       )
