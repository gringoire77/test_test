from sys import argv

#in1 = input('Введите ip-адрес в формате net/mask: ')
#ip, mask = in1.split('/')

ip = argv[1]

mask = argv[2]

ip = ip.split('.')

m1 = '1' * 32

m0 = '0' * 32

mask_str = m1[:int(mask)] + m0[int(mask):]

mask_list = (mask_str[0:8], mask_str[8:16], mask_str[16:24], mask_str[24:])

ip_net = [ int(ip[0], base=10)&int(mask_list[0], base=2), int(ip[1], base=10)&int(mask_list[1], base=2), int(ip[2], base=10)&int(mask_list[2], base=2), int(ip[3], base=10)&int(mask_list[3], base=2)]


ip_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_template = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:<08b}
'''


print('-' * 30)

print(ip_template.format(int(ip_net[0]),int(ip_net[1]),int(ip_net[2]),int(ip_net[3])))

print(mask_template.format(mask, int(mask_list[0], 2), int(mask_list[1], 2), int(mask_list[2], 2), int(mask_list[3], 2)))


#print (ip + ' ' +mask)
