# -*- coding: utf-8 -*-
from django.views.generic.detail import DetailView

from models import Page


class PageView(DetailView):

    """
    Class for view simple text page.
    """

    model = Page

    template_name = 'pages/page.html'

    slug_field = 'url'
    slug_url_kwarg = 'url'

    context_object_name = 'page'
