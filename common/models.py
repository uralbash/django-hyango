# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import TreeManager


class VisibleTreeManager(TreeManager):

    """
    Менеджер моделей с наследованием от менеджера MPTT
    """
    def get_query_set(self):
        return super(VisibleTreeManager, self).get_query_set()\
            .filter(visible=True)


class VisibleManager(models.Manager):
    def get_query_set(self):
        return super(VisibleManager, self).get_query_set().filter(visible=True)


class VisibleObject(models.Model):
    visible = visible = models.BooleanField(u'Показывать?', default=False)
    allpages = models.Manager()
    objects = VisibleManager()

    class Meta:
        abstract = True


class SEOModel(models.Model):
    seo_title = models.CharField(u'SEO-заголовок (title)', max_length=255,
                                 blank=True, null=True)
    seo_meta = models.TextField(u'SEO-мета (keywords, description)',
                                blank=True, null=True,
                                help_text=u'Вставьте сюда HTML-код мета'
                                u' информации:\nНапример:'
                                u' <meta name="keywords"'
                                u' content="Ключевые слова" />')

    class Meta:
        abstract = True


class VisibleSEOModel(VisibleObject, SEOModel):

    class Meta:
        abstract = True
