# -*- coding: utf-8 -*-
from django.db import models

from south.modelsinspector import add_introspection_rules

from common.fields import MultiEmailField
add_introspection_rules([], ["^pages\.fields\.MultiEmailField"])


class Settings(models.Model):
    site_name = models.CharField(u'Заголовок сайта', max_length=255)
    email = MultiEmailField(u'Email для формы оформления заказа',
                            max_length=255,
                            help_text=u'Можете вставить несколько email,'
                            + u' разделив их запятой')

    def __unicode__(self):
        return u'настройки'

    class Meta:
        verbose_name = u'настройки'
        verbose_name_plural = u'настройки'
