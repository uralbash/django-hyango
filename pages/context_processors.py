# -*- coding: utf-8 -*-
# Project`s apps
from pages.models import Page


def page(request):
    """
    Процессор добавляет элементы связанные с моделью 'Page'.
    """
    return {
        'header_menu': Page.objects.filter(in_header=True),  # Верхнее меню
    }
