Функция sorted
--------------

Функция ``sorted()`` возвращает новый отсортированный список, который
получен из итерируемого объекта, который был передан как аргумент.
Функция также поддерживает дополнительные параметры, которые позволяют
управлять сортировкой.

Первый аспект, на который важно обратить внимание - sorted возвращает
список.

Если сортировать список элементов, то возвращается новый список:

.. code:: python

    In [1]: list_of_words = ['one', 'two', 'list', '', 'dict']

    In [2]: sorted(list_of_words)
    Out[2]: ['', 'dict', 'list', 'one', 'two']

При сортировке кортежа также возвращается список:

.. code:: python

    In [3]: tuple_of_words = ('one', 'two', 'list', '', 'dict')

    In [4]: sorted(tuple_of_words)
    Out[4]: ['', 'dict', 'list', 'one', 'two']

Сортировка множества:

.. code:: python

    In [5]: set_of_words = {'one', 'two', 'list', '', 'dict'}

    In [6]: sorted(set_of_words)
    Out[6]: ['', 'dict', 'list', 'one', 'two']

Сортировка строки:

.. code:: python

    In [7]: string_to_sort = 'long string'

    In [8]: sorted(string_to_sort)
    Out[8]: [' ', 'g', 'g', 'i', 'l', 'n', 'n', 'o', 'r', 's', 't']

Если передать sorted словарь, функция вернет отсортированный список
ключей:

.. code:: python

    In [9]: dict_for_sort = {
       ...:         'id': 1,
       ...:         'name':'London',
       ...:         'IT_VLAN':320,
       ...:         'User_VLAN':1010,
       ...:         'Mngmt_VLAN':99,
       ...:         'to_name': None,
       ...:         'to_id': None,
       ...:         'port':'G1/0/11'
       ...: }

    In [10]: sorted(dict_for_sort)
    Out[10]:
    ['IT_VLAN',
     'Mngmt_VLAN',
     'User_VLAN',
     'id',
     'name',
     'port',
     'to_id',
     'to_name']

reverse
~~~~~~~

Флаг reverse позволяет управлять порядком сортировки. По умолчанию
сортировка будет по возрастанию элементов.

Указав флаг reverse, можно поменять порядок:

.. code:: python

    In [11]: list_of_words = ['one', 'two', 'list', '', 'dict']

    In [12]: sorted(list_of_words)
    Out[12]: ['', 'dict', 'list', 'one', 'two']

    In [13]: sorted(list_of_words, reverse=True)
    Out[13]: ['two', 'one', 'list', 'dict', '']

key
~~~

С помощью параметра key можно указывать, как именно выполнять
сортировку. Параметр key ожидает функцию, с помощью которой должно быть
выполнено сравнение.

Например, таким образом можно отсортировать список строк по длине
строки:

.. code:: python

    In [14]: list_of_words = ['one', 'two', 'list', '', 'dict']

    In [15]: sorted(list_of_words, key=len)
    Out[15]: ['', 'one', 'two', 'list', 'dict']

Если нужно отсортировать ключи словаря, но при этом игнорировать регистр
строк:

.. code:: python

    In [16]: dict_for_sort = {
        ...:         'id': 1,
        ...:         'name':'London',
        ...:         'IT_VLAN':320,
        ...:         'User_VLAN':1010,
        ...:         'Mngmt_VLAN':99,
        ...:         'to_name': None,
        ...:         'to_id': None,
        ...:         'port':'G1/0/11'
        ...: }

    In [17]: sorted(dict_for_sort, key=str.lower)
    Out[17]:
    ['id',
     'IT_VLAN',
     'Mngmt_VLAN',
     'name',
     'port',
     'to_id',
     'to_name',
     'User_VLAN']

Параметру key можно передавать любые функции, не только встроенные.
Также тут удобно использовать анонимную функцию lambda.

С помощью параметра key можно сортировать объекты не по первому
элементу, а по любому другому. Но для этого надо использовать или
функцию lambda, или специальные функции из модуля operator.

Например, чтобы отсортировать список кортежей из двух элементов по
второму элементу, надо использовать такой прием:

.. code:: python

    In [18]: from operator import itemgetter

    In [19]: list_of_tuples = [('IT_VLAN', 320),
        ...:  ('Mngmt_VLAN', 99),
        ...:  ('User_VLAN', 1010),
        ...:  ('DB_VLAN', 11)]

    In [20]: sorted(list_of_tuples, key=itemgetter(1))
    Out[20]: [('DB_VLAN', 11), ('Mngmt_VLAN', 99), ('IT_VLAN', 320), ('User_VLAN', 1010)]

