# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from website.views import IndexView
from common.seo import sitemaps


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),

                       # Sitemap & SEO
                       url(r'^sitemap\.xml$',
                           'django.contrib.sitemaps.views.sitemap',
                           {'sitemaps': sitemaps}),
                       url(r'^robots\.txt$', 'common.seo.robots'),
                       url(r'^favicon\.ico$', 'common.seo.favicon'),

                       # Captcha
                       url(r'^captcha/(?P<code>[\da-f]{32})/$',
                           'supercaptcha.draw'),
                       )

# Gallery
from gallery.urls import urlpatterns as gallery_urls
urlpatterns += gallery_urls

# Common
from website.urls import urlpatterns as website_urls
urlpatterns += website_urls

# Pages urls must be last pattern
from pages.urls import urlpatterns as pages_urls
urlpatterns += pages_urls
