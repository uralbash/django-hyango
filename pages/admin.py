# -*- coding: utf-8 -*-
# CORE
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Current project
from pages.models import Page
from grappelli_modeltranslation.admin import TranslationAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

class PageAdmin(DjangoMpttAdmin):
    list_display = ['name', 'path']
    fieldsets = [
        (None, {
            'fields': ['name', 'url', 'parent', 'redirect_to', ('visible',
                       'lock'), ('in_header', 'in_main', 'in_footer')],
            'classes': []
        }),
        (_(u'Содержимое страницы'), {
            'fields': ['content'],
            'classes': ['grp-collapse', 'grp-open']
        }),
        (_(u'SEO'), {
            'fields': ['seo_title', 'seo_meta'],
            'classes': ['grp-collapse', 'grp-closed']
        }),
    ]
    prepopulated_fields = {
        'url': ('name',),
        'seo_title': ('name',),
    }


admin.site.register(Page, PageAdmin)
