import sys

#print (sys.argv)

access_template = ['switchport mode access',
                                      'switchport access vlan {}',
                                      'switchport nonegotiate',
                                      'spanning-tree portfast',
                                      'spanning-tree bpduguard enable']

print('\n'.join(access_template).format(sys.argv[1]))
