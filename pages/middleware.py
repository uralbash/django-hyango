# -*- coding: utf-8 -*-
# CORE
from django.shortcuts import redirect

# Project`s apps
from pages.models import Page


class PageMiddleware(object):

    """
    Add page object to request object
    """
    def __init__(self):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):

        url = view_kwargs.get('url', request.path[:-1])

        if not url:
            url = '/'

        try:
            page = Page.objects.get(path=url)
        except Page.DoesNotExist:
            page = False
        request.page = page

        if page and getattr(page, 'redirect_to', False):
            return redirect(page.redirect_to)

        return None
