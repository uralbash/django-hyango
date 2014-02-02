Джанго-Хуянго
=============

Квик старт
----------

1. Установка по `pip install -r requirements.txt`
2. Далее введим python manage.py syncdb и видим красное Г в консоле:
`ImportError: cannot import name SEOModel`
Очень информативный вывод, все сразу стало понятно.
    
    * 2.1 Прошел все модели в проекте, SEOModel не нашел, при учете что у меня gallery стоит в virtualenv
    * 2.2 может во вью? Во вью то же нету
    * 2.3 ищем по проекту тупо по всем фалам, ничё нету.
    * 2.4 идем в settings/apps.py и смотрим какое Г может это содержать(так на угад), смотрим сommon обана вот он в моделях, осталось найти где он импортируется неправильно.
    * 2.5 ради интереса запускаю сервер `python manage.py runserver` и получаю:
      
          File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/gallery/models.py", line 12, in <module>
        from website.models import SEOModel, VisibleModel
        ImportError: cannot import name SEOModel
        
т.е. в некоторых случаях джангу надо дебажить runserver'ом

Pages
-----

1. захожу в pages в админке
2. добавляю дерево
3. тыкаю по дереву что бы развернуть список и получаю:

`Error while loading the data from the server.`

![IMAGE](https://ыыы/django-hyango/raw/83970477173377254a912fd97dec3fb4fda171e3/pages_tree.png)

и трэйс:

    Internal Server Error: /admin/pages/page/tree_json/
    Traceback (most recent call last):
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/core/handlers/base.py", line 115, in get_response
        response = callback(request, *callback_args, **callback_kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django_mptt_admin/admin.py", line 50, in wrapper
        return self.admin_site.admin_view(view)(*args, **kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/utils/decorators.py", line 91, in _wrapped_view
        response = view_func(request, *args, **kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/views/decorators/cache.py", line 89, in _wrapped_view_func
        response = view_func(request, *args, **kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/contrib/admin/sites.py", line 202, in inner
        return view(request, *args, **kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django_mptt_admin/admin.py", line 157, in tree_json_view
        node = self.model.objects.get(id=node_id)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/db/models/manager.py", line 143, in get
        return self.get_query_set().get(*args, **kwargs)
      File "/home/uralbash/.virtualenvs/django-hyango/local/lib/python2.7/site-packages/django/db/models/query.py", line 404, in get
        self.model._meta.object_name)
    DoesNotExist: Page matching query does not exist.
    [16/Dec/2013 23:42:28] "GET /admin/pages/page/tree_json/?node=5&_=1387215746550 HTTP/1.1" 500 22668
    
бесполезный трейс и непонятная ошибка КРУТО! 

Если я зайду на адрес /admin/pages/page/tree_json/?node=5&_=1387215746550 то получу статический trace и хер знает куда bp вставить что бы хоть за че-то зацепиться.

Ставлю `django-extension` через pip и `wergzeug` что бы получить хоть какой то интерактив на том же трэйсе.

Запускаю командой `python manage.py runserver_plus`, отваливается `debug_toolbar`

Интерактивный трейс тоже мало полезен, джанга каким то чудом обходит то место которое все ломает, ГРЕБАННЫЙ СТЫД! Ошибка ищется тупым эникейством. Предполагая что `django` идеальна и в ней нет ошибок, `django_mptt_admin` в example работает хорошо, может быть что то в `Pages`??? Ад же какойто?
