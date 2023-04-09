# Найти сумму цифр трехзначного числа

x = int(input())
units = x % 10
tenth = (x % 100 - units) // 10
hundredths = x // 100

print(units + hundredths + tenth)
