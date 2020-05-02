.. raw:: latex

   \newpage

Задания
=======

.. include:: ./exercises_intro.rst

Задание 4.1
~~~~~~~~~~~

Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

.. code:: python

    NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"


In [1]: NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"                                     

In [2]: NAT.replace('Fast', 'Gigabit')                                                                               
Out[2]: 'ip nat inside source list ACL interface GigabitEthernet0/1 overload'



второй вариант


In [12]: NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"                                    
In [13]: temp = NAT.split()                                                                                          

In [14]: temp[7] = 'GigabitEthernet0/1'                                                                              

In [15]: ' '.join(temp)                                                                                              
Out[15]: 'ip nat inside source list ACL interface GigabitEthernet0/1 overload'




Задание 4.2
~~~~~~~~~~~

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные
темы.

.. code:: python

    mac = 'AAAA:BBBB:CCCC'


In [18]: mac = 'AAAA:BBBB:CCCC'                                                                                      

In [19]: mac.replace(':',".")                                                                                        
Out[19]: 'AAAA.BBBB.CCCC'

   

Задание 4.3
~~~~~~~~~~~

Получить из строки config список VLANов вида:
``['1', '3', '10', '20', '30', '100']``

Ограничение: Все задания надо выполнять используя только пройденные
темы.

.. code:: python

    config = 'switchport trunk allowed vlan 1,3,10,20,30,100'



In [27]: config                                                                                                      
Out[27]: 'switchport trunk allowed vlan 1,3,10,20,30,100'

In [28]: vlans = config.split() [4]                                                                                  

In [29]: vlans                                                                                                       
Out[29]: '1,3,10,20,30,100'




Задание 4.4
~~~~~~~~~~~

Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

.. code:: python

    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]


In [69]: vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]                                                           

In [70]: temp = set(vlans)                                                                                           

In [71]: vlans = list(temp)                                                                                          

In [72]: vlans.sort()                                                                                                

In [73]: vlans                                                                                                       
Out[73]: [1, 2, 3, 4, 10, 20, 30, 100]



Задание 4.5
~~~~~~~~~~~

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ``['1', '3', '8']``

Ограничение: Все задания надо выполнять используя только пройденные темы.

.. code:: python

    command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
    command2 = 'switchport trunk allowed vlan 1,3,8,9'


In [133]: command1 = 'switchport trunk allowed vlan 1,2,3,5,8'                                                       

In [134]: command2 = 'switchport trunk allowed vlan 1,3,8,9'                                                         

In [135]: command1 = command1[30:].split(',')                                                                        

In [136]: command2 = command2[30:].split(',')                                                                        

In [137]: temp1 = set(command1)                                                                                      

In [138]: temp2 = set(command2)                                                                                      

In [140]: temp1 & temp2                                                                                              
Out[140]: {'1', '3', '8'}

In [141]: vlans = list (temp1 & temp2)                                                                               

In [142]: vlans                                                                                                      
Out[142]: ['1', '3', '8']

    
    
Задание 4.6
~~~~~~~~~~~

Обработать строку ospf_route и вывести информацию на стандартный поток
вывода в виде:

::

    Protocol:               OSPF
    Prefix:                 10.0.24.0/24
    AD/Metric:              110/41
    Next-Hop:               10.0.13.3
    Last update:            3d18h
    Outbound Interface:     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные
темы.

.. code:: python

    ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'


In [1]: ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'   

In [2]: temp = ospf_route.split()                                                             
In [3]: template = ''' 
   ...: Protocol:\t\t\t{0} 
   ...: Prefix:\t\t\t\t{1} 
   ...: AD/Metric:\t\t\t{2} 
   ...: Next-hop:\t\t\t{3} 
   ...: Last update:\t\t\t{4} 
   ...: Outbound Interface:\t\t{5} 
   ...: '''


In [8]: print (template.format('OSPF', temp[1], temp[2].strip('[]'), temp[4], temp[5], temp[6]))    

Protocol:           OSPF
Prefix:             10.0.24.0/24
AD/Metric:          110/41
Next-hop:           10.0.13.3,
Last update:            3d18h,
Outbound Interface:     FastEthernet0/0



Задание 4.7
~~~~~~~~~~~

Преобразовать MAC-адрес mac в двоичную строку такого вида:
``101010101010101010111011101110111100110011001100``

Ограничение: Все задания надо выполнять используя только пройденные
темы.

::

    mac = 'AAAA:BBBB:CCCC'


In [42]: mac = 'AAAA:BBBB:CCCC'                                                                                 

In [43]: mac_hex = mac.split(':')                                                                               

In [44]: string = str(bin(int(mac_hex[0], 16)) + bin(int(mac_hex[1], 16)) + bin(int(mac_hex[2], 16)))           

In [45]: string.replace('0b','')                                                                                
Out[45]: '101010101010101010111011101110111100110011001100'


Задание 4.8
~~~~~~~~~~~

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

* первой строкой должны идти десятичные значения байтов
* второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:

* столбцами
* ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:

::

    10        1         1         1
    00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные
темы.

::

    ip = '192.168.3.1'


In [112]: ip = '192.168.3.1'                                                                                    

In [113]: ip = ip.split('.')                                                                                    

In [114]: template = ''' 
     ...: {0:<8} {1:<8} {2:<8} {3:<8} 
     ...: {0:08b} {1:08b} {2:08b} {3:08b} 
     ...: '''                                                                                                   

In [115]: print (template.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))                                  
192      168      3        1       
11000000 10101000 00000011 00000001


