# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.http import Http404, HttpResponse

from pages.models import Page
from django.db.models import Q


class PageSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Page.objects.all()

    def priority(self, obj):
        if obj.id == 1:
            return 1.0
        else:
            return float(pow(0.9, obj.level + 1))


sitemaps = {
    'pages': PageSitemap,
}


def favicon(request):
    path = os.path.join(settings.MEDIA_ROOT, 'uploads', 'seo', 'favicon.ico')
    if os.path.exists(path):
        return HttpResponse(open(path).read(), mimetype='image/x-icon')
    else:
        raise Http404


def robots(request):
    path = os.path.join(settings.MEDIA_ROOT, 'uploads', 'seo', 'robots.txt')
    if os.path.exists(path):
        return HttpResponse(open(path).read(), mimetype='text/plain')
    else:
        raise Http404


def google(request):
    path = os.path.join(
        settings.MEDIA_ROOT, 'uploads', 'seo', 'google.html')
    if os.path.exists(path):
        return HttpResponse(open(path).read(), mimetype='text/html')
    else:
        raise Http404


def yandex(request):
    path = os.path.join(
        settings.MEDIA_ROOT, 'uploads', 'seo', 'yandex.html')
    if os.path.exists(path):
        return HttpResponse(open(path).read(), mimetype='text/html')
    else:
        raise Http404