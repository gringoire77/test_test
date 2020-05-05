in1 = input('Введите ip-адрекс в формате net/mask: ')
ip, mask = in1.split('/')

ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b}{1:08b}{2:08b}{3:<08b}
'''

print('-' * 30)


#print (ip + ' ' +mask)
