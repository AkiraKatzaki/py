import random

def monetki(n):
    reshka = 0
    orel = 0
    for i in range(n):
        x = random.randint(0, 1)
        print(x) # Чтобы видеть как сгенерировались монетки
        if x == 0:
            orel += 1
        else:
            reshka += 1
    if orel > reshka:
        return reshka
    else:
        return orel


print(monetki(5))
