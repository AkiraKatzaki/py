# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. \
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е.билет с номером 385916 – счастливый, т.к. 3 + 8 + 5 = 9 + 1 + 6.
# Вам требуется написать программу, которая проверяет счастливость билета.

bilet = int(input())
first = bilet // 1000
second = bilet % 1000
# расчет первой тройки
a = first // 10
b = a % 10
a = first // 100 + b
first = first % 10 + a
# расчет второй тройки
a = second // 10
b = a % 10
a = second // 100 + b
second = second % 10 + a
print(first == second)