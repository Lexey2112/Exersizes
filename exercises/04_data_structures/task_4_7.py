# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"

mac=mac.replace(':','')
string1='{:b}{:b}{:b}{:b}{:b}{:b}{:b}{:b}{:b}{:b}{:b}{:b}'.format(int(mac[0], 16), int(mac[1], 16), int(mac[2], 16),
int(mac[3], 16), int(mac[4], 16), int(mac[5], 16),
int(mac[6], 16), int(mac[7], 16), int(mac[8], 16),
int(mac[9], 16), int(mac[10], 16), int(mac[11], 16))
print(string1)
