.. raw:: latex

   \newpage

Задания
=======

.. include:: ./pytest.rst

Задание 20.1
~~~~~~~~~~~~

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:

* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:

* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Задание 20.2
~~~~~~~~~~~~

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:

* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

::

    R1#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
    R2#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
    Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
    R3#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
    Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml

Задание 20.3
~~~~~~~~~~~~

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:

* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

::

    R1#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
    R2#sh arp
    Protocol  Address          Age (min)  Hardware Addr   Type   Interface
    Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
    Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
    Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
    R3#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
    Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands

.. code:: python

    commands = {'192.168.100.1': 'sh ip int br',
                '192.168.100.2': 'sh arp',
                '192.168.100.3': 'sh ip int br'}


Задание 20.3a
~~~~~~~~~~~~~

Создать функцию send_command_to_devices, которая отправляет
список указанных команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:

* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какие команды. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом каждой команды надо написать имя хоста и саму команду):

::

    R2#sh arp
    Protocol  Address          Age (min)  Hardware Addr   Type   Interface
    Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
    Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
    R1#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
    R1#sh arp
    Protocol  Address          Age (min)  Hardware Addr   Type   Interface
    Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
    Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
    R3#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
    Ethernet0/1                unassigned      YES NVRAM  administratively down down
    R3#sh ip route | ex -

    Gateway of last resort is not set

          10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
    O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
    O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0


Порядок команд в файле может быть любым.

Для выполнения задания можно создавать любые дополнительные функции, а также использовать функции созданные в предыдущих заданиях.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands

.. code:: python

    commands = {'192.168.100.1': ['sh ip int br', 'sh arp'],
                '192.168.100.2': ['sh arp'],
                '192.168.100.3': ['sh ip int br', 'sh ip route | ex -']}


Задание 20.4
~~~~~~~~~~~~

Создать функцию send_commands_to_devices, которая отправляет команду show или config на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.

Параметры функции:

* devices - список словарей с параметрами подключения к устройствам
* show - команда show, которую нужно отправить (по умолчанию, значение None)
* config - команды конфигурационного режима, которые нужно отправить (по умолчанию, значение None)
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

::

    R1#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
    Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
    R2#sh arp
    Protocol  Address          Age (min)  Hardware Addr   Type   Interface
    Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
    Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
    Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
    R3#sh ip int br
    Interface                  IP-Address      OK? Method Status                Protocol
    Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
    Ethernet0/1                unassigned      YES NVRAM  administratively down down

Пример вызова функции:

.. code:: python

    In [5]: send_commands_to_devices(devices, show='sh clock', filename='result.txt')

    In [6]: cat result.txt
    R1#sh clock
    *04:56:34.668 UTC Sat Mar 23 2019
    R2#sh clock
    *04:56:34.687 UTC Sat Mar 23 2019
    R3#sh clock
    *04:56:40.354 UTC Sat Mar 23 2019

    In [11]: send_commands_to_devices(devices, config='logging 10.5.5.5', filename='result.txt')

    In [12]: cat result.txt
    config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#logging 10.5.5.5
    R1(config)#end
    R1#config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R2(config)#logging 10.5.5.5
    R2(config)#end
    R2#config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R3(config)#logging 10.5.5.5
    R3(config)#end
    R3#

    In [13]: send_commands_to_devices(devices,
                                      config=['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0'],
                                      filename='result.txt')

    In [14]: cat result.txt
    config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R1(config)#router ospf 55
    R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
    R1(config-router)#end
    R1#config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R2(config)#router ospf 55
    R2(config-router)#network 0.0.0.0 255.255.255.255 area 0
    R2(config-router)#end
    R2#config term
    Enter configuration commands, one per line.  End with CNTL/Z.
    R3(config)#router ospf 55
    R3(config-router)#network 0.0.0.0 255.255.255.255 area 0
    R3(config-router)#end
    R3#


Для выполнения задания можно создавать любые дополнительные функции.
