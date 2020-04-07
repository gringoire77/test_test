.. raw:: latex

   \newpage

Задания
=======

.. include:: ./pytest.rst


Задание 25.1
~~~~~~~~~~~~

Создать класс Topology, который представляет топологию сети.

При создании экземпляра класса, как аргумент передается словарь, который описывает топологию.
Словарь может содержать дублирующиеся соединения.

Дублем считается ситуация, когда в словаре есть такие пары: ``('R1', 'Eth0/0'): ('SW1', 'Eth0/1') и ('SW1', 'Eth0/1'): ('R1', 'Eth0/0')``

В каждом экземпляре должна быть создана переменная topology, в которой содержится словарь топологии, но уже без дублей.

Пример создания экземпляра класса:

.. code:: python

    In [2]: top = Topology(topology_example)

    После этого, должна быть доступна переменная topology:

    In [3]: top.topology
    Out[3]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}


Пример топологии:

.. code:: python

    topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}



Задание 25.1a
~~~~~~~~~~~~~

Скопировать класс Topology из задания 25.1 и изменить его.

Если в задании 25.1 удаление дублей выполнялось в методе __init__,
надо перенести функциональность удаления дублей в метод _normalize.

При этом метод __init__ должен выглядеть таким образом:

.. code:: python

    class Topology:
        def __init__(self, topology_dict):
            self.topology = self._normalize(topology_dict)


Задание 25.1b
~~~~~~~~~~~~~

Изменить класс Topology из задания 25.1a или 25.1.

Добавить метод delete_link, который удаляет указанное соединение.
Метод должен удалять и зеркальное соединение, если оно есть.

Если такого соединения нет, выводится сообщение "Такого соединения нет".

Создание топологии

.. code:: python

    In [7]: t = Topology(topology_example)

    In [8]: t.topology
    Out[8]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление линка:

.. code:: python

    In [9]: t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))

    In [10]: t.topology
    Out[10]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление зеркального линка

.. code:: python

    In [11]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))

    In [12]: t.topology
    Out[12]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}

Если такого соединения нет, выводится сообщение:

.. code:: python

    In [13]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    Такого соединения нет

Задание 25.1c
~~~~~~~~~~~~~

Изменить класс Topology из задания 25.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.
Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии

.. code:: python

    In [1]: t = Topology(topology_example)

    In [2]: t.topology
    Out[2]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:

.. code:: python

    In [3]: t.delete_node('SW1')

    In [4]: t.topology
    Out[4]:
    {('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:

.. code:: python

    In [5]: t.delete_node('SW1')
    Такого устройства нет

Задание 25.1d
~~~~~~~~~~~~~

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует".
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует".


Пример создания топологии и добавления соединений

.. code:: python

    In [7]: t = Topology(topology_example)

    In [8]: t.topology
    Out[8]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

    In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

    In [10]: t.topology
    Out[10]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

    In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    Такое соединение существует

    In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    Cоединение с одним из портов существует


Задание 25.2
~~~~~~~~~~~~

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:

* _write_line - принимает как аргумент строку и отправляет на оборудование строку преобразованную
  в байты и добавляет перевод строки в конце. Метод _write_line должен использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод полученный с обрудования

Пример создания экземпляра класса:

.. code:: python

    In [2]: from task_25_2 import CiscoTelnet

    In [3]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}
       ...:

    In [4]: r1 = CiscoTelnet(**r1_params)

    In [5]: r1.send_show_command('sh ip int br')
    Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

Задание 25.2a
~~~~~~~~~~~~~

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, 
  полученные после обработки с помощью TextFSM. 
  При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами


Пример создания экземпляра класса:

.. code:: python

    In [1]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}

    In [2]: from task_25_2a import CiscoTelnet

    In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:

.. code:: python

    In [4]: r1.send_show_command('sh ip int br', parse=False)
    Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

    In [5]: r1.send_show_command('sh ip int br', parse=True)
    Out[5]:
    [{'intf': 'Ethernet0/0',
      'address': '192.168.100.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/1',
      'address': '192.168.200.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/2',
      'address': '190.16.200.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/3',
      'address': '192.168.130.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/3.100',
      'address': '10.100.0.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/3.200',
      'address': '10.200.0.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Ethernet0/3.300',
      'address': '10.30.0.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Loopback0',
      'address': '10.1.1.1',
      'status': 'up',
      'protocol': 'up'},
     {'intf': 'Loopback55',
      'address': '5.5.5.5',
      'status': 'up',
      'protocol': 'up'}]

Задание 25.2b
~~~~~~~~~~~~~

Скопировать класс CiscoTelnet из задания 25.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного режима или список команд.
Метод дожен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).

Пример создания экземпляра класса:

.. code:: python

    In [1]: from task_25_2b import CiscoTelnet

    In [2]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}

    In [3]: r1 = CiscoTelnet(**r1_params)

    Использование метода send_config_commands:

    In [5]: r1.send_config_commands('logging 10.1.1.1')
    Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

    In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
    Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'


Задание 25.2c
~~~~~~~~~~~~~

Скопировать класс CiscoTelnet из задания 25.2b и изменить метод send_config_commands добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:

* strict=True значит, что при обнаружении ошибки, необходимо сгенерировать исключение ValueError
* strict=False значит, что при обнаружении ошибки, надо только вывести на стандартный поток вывода сообщене об ошибке

Метод дожен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже). Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:

.. code:: python

    In [1]: from task_25_2c import CiscoTelnet

    In [2]: r1_params = {
       ...:     'ip': '192.168.100.1',
       ...:     'username': 'cisco',
       ...:     'password': 'cisco',
       ...:     'secret': 'cisco'}

    In [3]: r1 = CiscoTelnet(**r1_params)

    In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
    In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
    In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:

.. code:: python

    In [7]: print(r1.send_config_commands(commands, strict=False))
    При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
    При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
    При выполнении команды "i" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "i"
    conf t
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#logging 0255.255.1
                       ^
    % Invalid input detected at '^' marker.

    R1(config)#logging
    % Incomplete command.

    R1(config)#i
    % Ambiguous command:  "i"
    R1(config)#logging buffered 20010
    R1(config)#ip http server
    R1(config)#end
    R1#

    In [8]: print(r1.send_config_commands(commands, strict=True))
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-8-0abc1ed8602e> in <module>
    ----> 1 print(r1.send_config_commands(commands, strict=True))

    ...

    ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

