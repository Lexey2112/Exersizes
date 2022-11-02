# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip=input('введите айпи в формате 10.0.1.1: ')


try:
    ip_list=ip.split('.')
    int(ip_list[0]) and int(ip_list[1]) and int(ip_list[2]) and int(ip_list[3])
except:
  print("Неправильный IP-адрес")
else:
    if int(ip_list[0])>=0 and int(ip_list[0])<=255 and int(ip_list[1])>=0 and int(ip_list[1])<=255 and int(ip_list[2])>=0 and int(ip_list[2])<=255 and int(ip_list[3])>=0 and int(ip_list[3])<=255 and len(ip_list)==4:
        if int(ip_list[0])>1 and int(ip_list[0])<224:
            print('unicast')
        elif int(ip_list[0])>223 and int(ip_list[0])<240:
            print('multicast')
        elif ip=='0.0.0.0':
            print('unassigned')
        elif ip=='255.255.255.255':
            print('local broadcast')
        else:
            print('unused')
    else:
        print("Неправильный IP-адрес")
