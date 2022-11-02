# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""




result=False
while result !=True:
    try:
        ip=input('введите айпи в формате 10.0.1.1: ')
        ip_list=ip.split('.')
        int(ip_list[0]) and int(ip_list[1]) and int(ip_list[2]) and int(ip_list[3])
    except:
        print("Неправильный IP-адрес")
    else:
        if int(ip_list[0])>=0 and int(ip_list[0])<=255 and int(ip_list[1])>=0 and int(ip_list[1])<=255 and int(ip_list[2])>=0 and int(ip_list[2])<=255 and int(ip_list[3])>=0 and int(ip_list[3])<=255 and len(ip_list)==4:
            if int(ip_list[0])>1 and int(ip_list[0])<224:
                print('unicast')
                result=True
            elif int(ip_list[0])>223 and int(ip_list[0])<240:
                print('multicast')
                result=True
            elif ip=='0.0.0.0':
                print('unassigned')
                result=True
            elif ip=='255.255.255.255':
                print('local broadcast')
                result=True
            else:
                print('unused')
                result=True
        else:
            print("Неправильный IP-адрес")

