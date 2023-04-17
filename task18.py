'''
Задача 18:

Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

import random
num_n = int(input('Введите количество элементов N списка: '))
num_x = int(input('Введите число X: '))

list_input = [random.randint(0, 5) for i in range(num_n)]
print(f'Исходный список:\n{list_input} \n==============')

diff_elm = abs(list_input[0] - num_x)

index = 0
for i in range(num_n):
    if abs(list_input[i]-num_x) < diff_elm:
        diff_elm = abs(list_input[i]-num_x)
        index = i
print(f'Ближайший элемент к заданному X равен {list_input[index]}')
