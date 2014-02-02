# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

from pages.models import Banner


class IndexView(TemplateView):

    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        kwargs["banners"] = Banner.objects.all()

        return super(IndexView, self).get_context_data(**kwargs)
