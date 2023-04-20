# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

def search_nearest(n, x):
    j = n
    print('N = ', n)
    arr_list = []
    count = 0
    while count != n:
        z = int(input(f'Осталось ввести {j} чисел: '))
        arr_list.append(z)
        j -= 1
        count += 1
    print('Наш массив: ', arr_list)

    maximal = arr_list[0]  # поиск ближайшего максимума
    array = []
    for i in arr_list:
        while i > x:
            array.append(i)
            maximal = i
            break
    for i in array:
        if i < maximal:
            maximal = i
    print('ближайшее большее: ', maximal)

    minimal = arr_list[0]  # поиск ближайшего минимума
    for i in arr_list:
        if i < x and minimal < x and (x - i) < (x - minimal):
            minimal = i
    print('ближайшее меньшее: ', minimal)

    if x - minimal == maximal - x:   # сравнение ближайщих макс и мин
        a = maximal - x
        print(f'минимальное ближайшее {minimal} максимальное ближайшее {maximal} их разница c числом X = {x} равна {a}')
    elif x - minimal > maximal - x:
        a = maximal - x
        print(f'ближайшее число {maximal} их разница c числом X = {x} равна {a}')
    else:
        a = x - minimal
        print(f'ближайшее число {minimal} их разница c числом X = {x} равна {a}')

print(search_nearest(8, 10))