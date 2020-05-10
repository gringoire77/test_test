access_template = [
            'switchport mode access', 'switchport access vlan {}',
            'switchport nonegotiate', 'spanning-tree portfast',
            'spanning-tree bpduguard enable'
]


trunk_template = [
            'switchport trunk encapsulation dot1q', 'switchport mode trunk',
            'switchport trunk allowed vlan {}'
]


mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
vlan = input ('Введите номер влан(ов): ')


template = mode + '_template'

print ('\n')
print ('interface ',interface)
print (('\n'.join(eval(template))).format(vlan))
