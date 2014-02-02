# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import iri_to_uri

from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel, TreeForeignKey, TreeManager


class VisibleManager(models.Manager):

    """
    Менеджер моделей с наследованием от стандартного Django`вского менеджера.
    """
    def get_query_set(self):
        return super(VisibleManager, self).get_query_set().filter(visible=True)


class VisibleTreeManager(TreeManager):

    """
    Менеджер моделей с наследованием от менеджера MPTT
    """
    def get_query_set(self):
        return super(VisibleTreeManager, self).get_query_set()\
            .filter(visible=True)


class Page(MPTTModel):

    """
    Analog Django Flatpages framework.
    But used MPTT for create tree.
    """
    name = models.CharField(_(u'название'), max_length=255)
    path = models.CharField(_(u'полный путь на сайте'), max_length=255,
                            db_index=True, editable=False, unique=True)
    url = models.CharField(_(u'URL'), max_length=100,
                           help_text=u'''
Если первым символом указать "/", то путь страницы будет считаться от корня
сайта, иначе будет прибавлен к пути родителя. Примеры:
<br />1) /about => http://mysite.ru/about/
<br />2) contacts (является дочерней страницей страницы about) =>
http://mysite.ru/about/contacts''')
    content = tinymce_models.HTMLField(_(u'содержимое страницы'),
                               blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children',
                            verbose_name=_(u'родительский элемент'))
    redirect_to = models.CharField(_(u'перенаправить на страницу'),
                                   max_length=255, blank=True, null=True,
                                   help_text=u'''
В данное поле можно вводить как пути относительные для сайта, так и ведущие
на внешние ресурсы. Примеры:
<br />1) /about
<br />2) http://www.example.com/about/contacts''')
    visible = models.BooleanField(_(u'показывать?'), default=False)
    lock = models.BooleanField(_(u'заблокировать?'), default=False)
    in_header = models.BooleanField(_(u'отображать в верхнем меню?'),
                                    default=False)
    in_main = models.BooleanField(_(u'отображать в основном меню?'),
                                    default=False)
    in_footer = models.BooleanField(_(u'отображать в нижнем меню?'),
                                    default=False)

    seo_title = models.CharField(_(u'заголовок (title)'), max_length=255,
                                 blank=True, null=True)
    seo_meta = models.TextField(_(u'мета-дескрипторы (meta)'),
                                blank=True, null=True)

    allpages = TreeManager()
    objects = VisibleTreeManager()
    tree = TreeManager()

    def get_absolute_url(self):
        return iri_to_uri(self.path)

    def save(self, *args, **kwargs):
        self.url = self.url.strip()
        # Absolute URL
        absolute = self.url.startswith('/')
        if absolute:
            self.path = self.url
        else:
            self.path = '/%s' % self.url
        parent_path = getattr(self.parent, 'path', '/')
        if not absolute and parent_path != '/':
            self.path = ''.join([self.parent.path, self.path])
        if self.path != '/':
            self.path = self.path.rstrip('/')
        super(Page, self).save(*args, **kwargs)
        # Update children
        children = self.get_children()
        for child in children:
            child.save()

    def delete(self, *args, **kwargs):
        if self.lock:
            return False
        super(Page, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('path', 'url', 'name')
        verbose_name = _(u'страница')
        verbose_name_plural = _(u'страницы сайта')


class Banner(models.Model):
    """ Banner из erta
    """
    name = models.CharField(u'Название', max_length=255)
    image = FileBrowseField(u'Изображение', max_length=255,
                            blank=True, null=True)
    text = tinymce_models.HTMLField(u'Текст', blank=True, null=True)
    url = models.CharField(u'Ссылка', max_length=255, blank=True, null=True)
    visible = models.BooleanField(u'Показывать', default=True)
    sort = models.IntegerField(u'Порядок', default=0)

    allobjects = models.Manager()
    objects = VisibleManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('sort', 'name',)
        verbose_name = u'ротатор'
        verbose_name_plural = u'ротаторы'
