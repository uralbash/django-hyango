# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
# CORE
from django.db import IntegrityError
from django.test import TestCase

# Project`s apps
from pages.models import Page


class PageTest(TestCase):

    """
    Тест-кейс базовых возможностей модели 'Page'.
    """

    def setUp(self):
        self.page, self.root_created = Page.objects\
            .get_or_create(path='/', level=0,
                           defaults={'name': 'Root', 'url': '/', 'lock': True})

    def test_create_ununiq_root(self):
        """
        Создание страницы с уровнем (атрибут 'level') равным 0 и полным путём
        (атрибут 'path') '/' должно выдавать ошибку.
        Т.к. запись с такими данными добавляется при инициализации приложения.
        """
        with self.assertRaises(IntegrityError):
            Page.objects.create(name='Foo', url='/')

    def test_create_ununiq_child(self):
        """
        Создание страницы с уровнем (атрибут 'level') больше 0 и URL`ом
        совпадающим с "родителем" должно выдавать ошибку.
        """
        with self.assertRaises(IntegrityError):
            Page.objects.create(name='Foo', url=self.page.url,
                                parent=self.page)

    def test_lock_delete(self):
        """
        Попытка удаления заблокированной записи (lock = True) должна
        возвращать False.
        """
        page = self.page
        if not page.lock:
            page = Page.objects.create(name='Foo', url='foo', lock=True)
        self.assertFalse(page.delete())

    def test_inherit_path(self):
        """
        При создании "ребёнка" с относительным URL`ом его полный путь
        (атрибут 'path') должен включать путь "родителя".
        """
        ap_url = '/absolute-parent'  # URL "родителя"
        rc_url = 'relative-child'  # URL "ребёнка"
        parent = Page.objects.create(name='AbsoluteParent', url=ap_url)
        child = parent.children.create(name='RelativeChild', url=rc_url)
        self.assertEqual(child.path, '/'.join([ap_url, rc_url]))

    def test_update_inherit_path(self):
        """
        При изменении URL`а у "родителя" должен смениться полный путь (атрибут
        'path') у всех "потомков".
        """
        ap_url_init = '/absolute-parent-init'  # URL "родителя" при создании
        ap_url_change = '/absolute-parent-change'  # --//-- после изменения
        rc_url_init = 'relative-child-init'  # URL "ребёнка" при создании
        parent = Page.objects.create(name='AbsoluteParent', url=ap_url_init)
        parent.children.create(name='RelativeChild', url=rc_url_init)
        parent.url = ap_url_change
        parent.save()
        child = parent.get_children()[0]
        self.assertEqual(child.path, '/'.join([ap_url_change, rc_url_init]))

    def test_remove_children(self):
        """
        При удалении "родителя" должны удаляться все "потомки".
        """
        parent = Page.objects.create(name='ParentWillDelete',
                                     url='parent-will-delete')
        child_pk = parent.children.create(name='ChildWillDelete',
                                          url='child-will-delete').pk
        parent.delete()
        with self.assertRaises(Page.DoesNotExist):
            Page.objects.get(pk=child_pk)

    def test_remove_last_slash_in_path(self):
        """
        В полном пути (атрибут 'path') не должно быть закрывающего слеша.
        """
        page = Page.objects.create(name='SimplePage', url='simple-page/')
        self.assertEqual(page.path, '/simple-page')
