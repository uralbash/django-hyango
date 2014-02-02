# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse, Http404
from django.core.urlresolvers import resolve
from pages.models import Page


class JSONResponseMixin(object):

    """
    Миксин добавляет метод для возврата JSON'а
    """

    def json_to_response(self, context, **response_kwargs):
        """Convert the context dictionary into a JSON object"""
        json_data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(json_data, **response_kwargs)


class SEOMixin(object):
    """
    Миксин для добавления SEO'шной инфы в контекст.
    """

    def get_context_data(self, **kwargs):
        obj = getattr(self, 'object', False)
        if obj:
            kwargs['seo_title'] = getattr(obj, 'seo_title', None)
            kwargs['seo_meta'] = getattr(obj, 'seo_meta', None)
        context = super(SEOMixin, self).get_context_data(**kwargs)
        return context


class PagePrefixMixin(object):


    def get_context_data(self, **kwargs):
        page_prefix = self.kwargs.get('page_prefix', None)
        kwargs['page_prefix'] = page_prefix
        if page_prefix and not Page.objects.filter(path=page_prefix[:-1]).exists():
            raise Http404
        return super(PagePrefixMixin, self).get_context_data(**kwargs)
