Основы ООП
----------

-  Класс (class) - элемент программы, который описывает какой-то тип
   данных. Класс описывает шаблон для создания объектов, как правило,
   указывает переменные этого объекта и действия, которые можно
   выполнять применимо к объекту.
-  Экземпляр класса (instance) - объект, который является представителем
   класса.
-  Метод (method) - функция, которая определена внутри класса и
   описывает какое-то действие, которое поддерживает класс
-  Переменная экземпляра (instance variable, а иногда и instance
   attribute) - данные, которые относятся к объекту
-  Переменная класса (class variable) - данные, которые относятся к
   классу и разделяются всеми экземплярами класса
-  Атрибут экземпляра (instance attribute) - переменные и методы,
   которые относятся к объектам (экземплярам) созданным на основании
   класса. У каждого объекта есть своя копия атрибутов.

Пример из реальной жизни в стиле ООП:

-  Проект дома - это класс
-  Конкретный дом, который был построен по проекту - экземпляр класса
-  Такие особенности как цвет дома, количество окон - переменные
   экземпляра, то есть конкретного дома
-  Дом можно продать, перекрасить, отремонтировать - это методы

Рассмотрим практический пример использования ООП.

В разделе "18. Работа с базами данных" первое, что нужно было сделать
для работы с БД, подключиться к ней:

.. code:: python

    In [1]: import sqlite3

    In [2]: conn = sqlite3.connect('dhcp_snooping.db')

Переменная ``conn`` - это объект, который представляет реальное
соединение с БД. Благодаря функции type, можно выяснить экземпляром
какого класса является объект conn:

.. code:: python

    In [3]: type(conn)
    Out[3]: sqlite3.Connection

У conn есть свои методы и переменные, которые зависят от состояния
текущего объекта. Например, переменная экземпляра conn.in_transaction
доступна у каждого экземпляра класса sqlite3.Connection и возвращает
True или False, в зависимости от того все ли изменения закоммичены:

.. code:: python

    In [15]: conn.in_transaction
    Out[15]: False

Метод execute выполняет команду SQL:

.. code:: python

    In [19]: query = 'insert into dhcp (mac, ip, vlan, interface) values (?, ?, ?, ?)'

    In [5]: conn.execute(query, ('0000.1111.7777', '10.255.1.1', '10', 'Gi0/7'))
    Out[5]: <sqlite3.Cursor at 0xb57328a0>

При этом, объект conn сохраняет состояние: теперь переменная экзепляра
conn.in_transaction, возвращает True:

.. code:: python

    In [6]: conn.in_transaction
    Out[6]: True

После вызова метода commit, она опять равна False:

.. code:: python

    In [7]: conn.commit()

    In [8]: conn.in_transaction
    Out[8]: False

В этом примере показаны важные аспекты ООП: объединение данных и
действия над данными, а также сохранение состояния.

До сих пор, при написании кода, данные и действия на данными были
разделены. Чаще всего, действия описаны в виде функций, а данные
передаются как аргументы этим функциям. При создании класса, данные и
действия объединяются. Конечно же, это данные и действия связаны. То
есть, методами класса становятся те действия, которые характерны именно
для объекта такого типа, а не какие-то произвольные действия.

Например, в экзепляре класса str, все методы относятся к работе с этой
строкой:

.. code:: python

    In [10]: s = 'string'

    In [11]: s.upper()
    Out[11]: 'STRING'

    In [12]: s.center(20, '=')
    Out[12]: '=======string======='


.. note::

    На примере со строкой понятно, что класс не обязан хранить
    состояние - строка неизменяемый тип данных и все методы возвращают
    новые строки и не изменяют исходную строку.

Выше, при обращении к атрибутам экземпляра (переменным и методам)
используется такой синтаксис: ``objectname.attribute``. Эта запись
``s.lower()`` означает: вызвать метод lower у объекта s. Обращение к
методам и переменным выполняется одинаково, но для вызова метода, надо
добавить скобки и передать все необходимые аргументы.

Всё описанное неоднократно использовалось в книге, но теперь мы
разберемся с формальной терминологией.

