# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Gallery, GalleryImage
from grappelli_modeltranslation.admin import TranslationAdmin


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


class GalleryAdmin(TranslationAdmin):
    fieldsets = [
        (None, {
            'fields': ['visible', 'name', 'date', 'description_short',
                       'directory', 'description', ]
        }),
        (u'SEO-информация', {
            'fields': ['seo_title', 'seo_meta', ],
            'classes': ['grp-collapse', 'grp-closed']
        }),
    ]
    inlines = [GalleryImageInline]
    list_display = ('__unicode__', 'date', 'visible', 'directory', )
    list_display_links = ('__unicode__', 'date', )
    list_editable = ('visible', 'directory', )
    list_filter = ('visible', )
    search_fields = ['name', 'date', ]

admin.site.register(Gallery, GalleryAdmin)
