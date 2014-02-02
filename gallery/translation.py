# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from models import Gallery


class GalleryTranslationOptions(TranslationOptions):

    fields = ('name', 'description_short', 'description',
              'seo_title', 'seo_meta')

translator.register(Gallery, GalleryTranslationOptions)
