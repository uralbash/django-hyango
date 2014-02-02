# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField

from common.models import SEOModel, VisibleObject

from managers import GalleryImageFBManager


class Gallery(SEOModel, VisibleObject):
    name = models.CharField(_(u'Название'), max_length=255)
    date = models.DateField(_(u'Дата добавления'), editable=True,
                            default=datetime.date.today)
    description_short = models.TextField(_(u'Краткое описание'),
                                         blank=True, null=True)
    description = HTMLField(_(u'Описание'), blank=True, null=True)
    directory = models.CharField(
        _(u'Каталог с изображениями'), max_length=255,
        blank=True, null=True,
        help_text=_(u'Путь относительно каталога /media/.'))

    class Meta:
        ordering = ('date', 'name',)
        verbose_name = _(u'Фото галерея')
        verbose_name_plural = _(u'Фото галереи')

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse_lazy('gallery_detail', args=[self.pk])

    def save(self):
        """Переопределённый метод сохранения экземпляра модели.

        Перед сохранением убираем из поля 'directory' часть, содержащую
        settings.MEDIA_URL без начального слеша ('/').
        """
        self.directory = self.directory.lstrip('/')
        media_relative_url = settings.MEDIA_URL.lstrip('/')
        self.directory = self.directory.replace(media_relative_url, '', 1)
        return super(Gallery, self).save()

    def get_first_image(self):
        fl = GalleryImageFBManager().get_filelisting(self.directory)
        if len(fl) > 0:
            return fl[0]
        images = self.images.all()
        if images.exists():
            return images[0].image
        return None

    def get_images_count(self):
        fl = GalleryImageFBManager().get_filelisting(self.directory)
        if len(fl) > 0:
            return len(fl)
        return self.images.all().count()


class GalleryImage(VisibleObject):
    gallery = models.ForeignKey(Gallery, verbose_name=_(u'галерея'),
                                related_name='images')
    image = FileBrowseField(_(u"изображение"), format='image', max_length=255,
                            blank=True, null=True)
    description = models.TextField(_(u'Описание'), blank=True, null=True)

    fb_objects = GalleryImageFBManager()

    class Meta:
        verbose_name = _(u'изображение')
        verbose_name_plural = _(u'изображения')
