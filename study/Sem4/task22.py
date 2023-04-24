# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


array_list = list()
a = int(input('Введите размер 1 списка: '))
for temp_var in range(a):
    temp_var = int(input('Введите число: '))
    array_list.append(temp_var)

array_list2 = list()
b = int(input('Введите размер 2 списка: '))
for temp_var in range(b):
    temp_var = int(input('Введите число: '))
    array_list2.append(temp_var)
print(array_list, array_list2)

array_list.extend(array_list2)
print(array_list)
x = set(array_list)
print(x)
