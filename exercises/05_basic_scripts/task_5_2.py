# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip=input('ввод IP-сети в формате: 10.1.1.0/24: ')

template='''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4:<}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''
#10.1.1.0/24
ip=ip.split('.')
ip1,ip2,ip3,ip4=int(ip[0]),int(ip[1]),int(ip[2]),ip[3]
ip4, pref=int(ip4.split('/')[0]), ip4.split('/')[1]
#pref=24
pref_str=pref
pref_A=int(pref)
pref_end=32-pref_A
pref="1" * pref_A + "0" * pref_end
pref1,pref2,pref3,pref4=int(pref[0:8], 2), int(pref[8:16], 2), int(pref[16:24], 2), int(pref[24::], 2)
print(template.format(ip1,ip2,ip3,ip4,pref_str,pref1,pref2,pref3,pref4))