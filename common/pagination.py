#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Mixin for pagination
"""
from django.core.paginator import Paginator, InvalidPage, EmptyPage


class SlicePaginatorMixin(object):

    """
    Миксин для красивой постранички.
    Т.е. изначально постраничка выглядит примерно так:
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    А даанный миксин позволяет сдалть так (при 'pages_forward = 5'):
        Выбрана 1-я страница:   <1> 2 3 4 5 6 ... 15
        Выбрана 2-я страница:   1 <2> 3 4 5 6 ... 15
        Выбрана 3-я страница:   1 2 <3> 4 5 6 ... 15
        Выбрана 4-я страница:   1 2 3 <4> 5 6 ... 15
        Выбрана 5-я страница:   1 ... 3 4 <5> 6 7 ... 15
        ...
        Выбрана 13-я страница:   1 ... 11 12 <13> 14 15
    """
    pages_forward = 5
    paginate_by = 10

    def paginate_queryset(self, queryset, page_size):
        paginator, page, object_list, is_paginated = super(
            SlicePaginatorMixin, self).paginate_queryset(queryset, page_size)
        slice__start = 0
        slice__end = paginator.num_pages
        is_sliced = False
        if paginator.num_pages - 2 > self.pages_forward:
            slice__end = self.pages_forward + 1
            is_sliced = True
        show__half = self.pages_forward / 2
        # Смотри "Выбрана 5-я страница"
        if is_sliced and page.number - show__half > 2:
            slice__start = page.number - show__half - 1
        # Смотри "Выбрана 5-я страница"
        if is_sliced and page.number + show__half > self.pages_forward + 1:
            slice__end = page.number + show__half
        # Смотри "Выбрана 13-я страница"
        if is_sliced and page.number + show__half > paginator.num_pages - 2:
            slice__start = paginator.num_pages - self.pages_forward - 1
            slice__end = paginator.num_pages
        paginator.slice = '%s:%s' % (slice__start, slice__end)
        return (paginator, page, object_list, is_paginated)


def get_paginator(request, queryset, rows_on_page=None, pages_forward=None):
    DEFAULT_ROWS_ON_PAGE = 30
    DEFAULT_PAGES_FORWARD = 5
    rows_on_page = rows_on_page or DEFAULT_ROWS_ON_PAGE
    pages_forward = pages_forward or DEFAULT_PAGES_FORWARD

    paginator = Paginator(queryset, rows_on_page, orphans=0)
    try:
        page = int(request.REQUEST.get('page', '1'))
    except ValueError:
        page = 1
    try:
        objects = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)

    start_index = page - (pages_forward+1)
    if start_index < 0:
       start_index = 0
    objects.paginator.slice = "%d:%d" % (start_index, page+pages_forward)
    return objects


def get_paginator_slice(request, rows_on_page=None, pages_forward=None):
    DEFAULT_ROWS_ON_PAGE = 30
    DEFAULT_PAGES_FORWARD = 5
    rows_on_page = rows_on_page or DEFAULT_ROWS_ON_PAGE
    pages_forward = pages_forward or DEFAULT_PAGES_FORWARD
    try:
        page = int(request.REQUEST.get('page', '1'))
    except ValueError:
        page = 1

    start_index = page - (pages_forward + 1)
    if start_index < 0:
        start_index = 0
    paginator_slice = "%d:%d" % (start_index, page + pages_forward)
    return paginator_slice
