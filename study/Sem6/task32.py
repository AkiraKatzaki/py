'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

def i_array(array, min_n, max_n):
    temp = list()
    print(array)
    for i in range(len(array)):
        if min_n <= array[i] <= max_n:
            temp.append(i)
    return temp

array = [1, 3, 7, 10, 5, 8]
min_n = int(input('Введите минимум: '))
max_n = int(input('Введите максимум: '))
print(i_array(array, min_n, max_n))