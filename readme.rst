Longbow: сервис тестирования знаний
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:time-stamp: 02.08.2018 19:37:47
:tags: Python Django Тестовые задания

.. contents::

`Репозиторий <https://github.com/NameRec/longbow>`__.

Задание
=======

`Источник <https://docs.google.com/document/d/1tHdACMt7giCMk_J4LBDntLrsFd2LlDhKPzHriR0dO0g/edit>`__.

Задание сформулировано довольно широко, что позволит Вам продемонстрировать знания.

Необходимо создать сервис проведения тестирования. Тесты имеют определенный порядок вопросов. У вопроса может быть один или несколько вариантов правильных ответов, пропуск вопросов не допускается.

Пользователь должен пройти регистрацию или авторизоваться, чтобы приступить к тестированию. Зарегистрированный пользователь может пройти любой тест, после завершения теста видит результат, количество правильных/неправильных ответов и процент правильных ответов. Тест можно пройти только один раз.

Администратор может редактировать любой из тестов и добавлять новые. Посмотреть статистику по пользователю.

Результат должен быть выложен на GitHub

Должен запускаться на Python 3.5 и Django 1.11 или более поздних версиях.

Список всех зависимостей должен храниться в ``requirements.txt``, соответственно можно установить их командой ``pip install -r requirements.txt``.

По фронту требований никаких не предъявляется. Интерфейс не будет оцениваться.

Как плюс:
    Упаковать приложение в Docker-контейнер, который можно собрать и запустить локально.

    Контейнер должен подниматься одной командой (``docker run`` или ``docker-compose``).

    Файл ``readme`` должен содержать описание как работать с приложением, запускать тесты.

    Приложение должно быть доступно локально на 80 порту.

    Приложение должно быть покрыто unit-тестами (на чем будут написаны тесты не имеет значения).

Полезные ссылки
===============

Официальные материалы
---------------------

*   Официальная документация Django `для v1.9 <https://djbook.ru/rel1.9/>`__, `для v2.1 (англ.) <https://docs.djangoproject.com/en/2.1/>`__.
*   Создаём своё первое приложение с Django `для v1.9 (рус.) <https://djbook.ru/rel1.9/intro/tutorial01.html>`__, `для v2.1 (англ.) <https://docs.djangoproject.com/en/2.1/intro/>`__.
*   `Glossary - терминолония Django (англ.) <https://docs.djangoproject.com/en/2.1/glossary/#term-project>`__.
*   Интерфейс администратора `для v1.8 (рус) <https://djbook.ru/rel1.9/ref/contrib/admin/index.html>`__, `для v2.1 (англ.) <https://docs.djangoproject.com/en/2.1/ref/contrib/admin/>`__.
*   `Аутентификация пользователей в Django <https://djbook.ru/rel1.9/topics/auth/index.html>`__.
*   django-admin и manage.py: `Введение <https://djbook.ru/rel1.9/ref/django-admin.html>`__, `Реализация собственных команд <https://djbook.ru/rel1.9/howto/custom-management-commands.html>`__.

Конкретные рекомендации
-----------------------

*   Админка

    *   `django-ordered-model <https://github.com/bfirsh/django-ordered-model>`__.

        Поддержка порядка записей в моделях Django.

        Комментарий автора:

            django-ordered-model allows models to be ordered and provides a simple admin interface for reordering them.

            Based on https://djangosnippets.org/snippets/998/ and https://djangosnippets.org/snippets/259/

    *   `Django Admin nested inline <https://stackoverflow.com/a/22113967>`__ - интересное интерфейсное решение, обеспечивающая возможность изменения записи, отображаемой в inline-списке админки.

        Суть рекомендации в следующем:

            One common way around this is to link to an admin between first and second (or second and third) level by having both a ModelAdmin and an Inline for the same model:

            Give Certificate a ModelAdmin with TrainingDate as an inline. Give CertificateInline an additional field "Details" which is a link to its ModelAdmin change form.

        Интересен также `другой ответ <https://stackoverflow.com/a/22113967>`__, не требующий, вроде как, внесения изменений в модель.

    *   `django-inline-actions <https://github.com/escaped/django-inline-actions>`__.

            django-inline-actions adds actions to the InlineModelAdmin and ModelAdmin changelist.

        Вроде бы, закрывает тему редактирования элемента inline-списка, обеспечивая возможность расположения ссылок (в виде кнопок) для выполнения действий над элементом списка.

        Беда только, что не работает с Django 2.1.

    *   **Использованное решение:** `django-admin-sortable2 <https://github.com/jrief/django-admin-sortable2>`__ - немного топорно, но работает.

*   `django - comparing old and new field value before saving <https://stackoverflow.com/a/23363123>`__.

    Немного не в тему, но всё равно полезно насчёт ``:OLD_VALUES``.

*   `Manipulating Data in Django's Admin Panel on Save <https://stackoverflow.com/a/753722>`__, `Django admin: override delete method <https://stackoverflow.com/a/15196567>`__.

    Перехват операций изменения данных из админки Django. Техника логична, и достаточно проста: нужно перекрывать действия ``save_model`` и ``delete_model`` у потомка ``admin.ModelAdmin``.

*   Регистрация и аутентификация пользователей

    *   `Django: регистрация и аутентификация пользователей <https://ustimov.org/posts/17/>`__.

        Описан процесс регистрации нового пользователя через встроенные в Django возможности.

    *   `How to Create User Sign Up View <https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-profile-model>`__.

        Подробно описан процесс регистрации нового пользователя. Репозиторий `готовых решений <https://github.com/sibtc/simple-signup>`__.

*   Динамическое создание форм

    *   Обсуждение `"Автоматическое создание полей формы для формы в django" <http://qaru.site/questions/20406/auto-generate-form-fields-for-a-form-in-django>`__.

    *   Статья `So you want a dynamic form <https://www.b-list.org/weblog/2008/nov/09/dynamic-forms/>`__.

    *   Статья `Динамическое создание форм на основе данных из базы в Django <https://habr.com/post/46845/>`__.
