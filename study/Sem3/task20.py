# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность.

def scrabble(ver, word):
    rus = {1: 'АВЕИНОРСТ',
           2: 'ДКЛМПУ',
           3: 'БГЁЬЯ',
           4: 'ЙЫ',
           5: 'ЖЗХЦЧ',
           8: 'ШЭЮ',
           10: 'ФЩЪ'}
    eng = {1: 'AEIOULNSTR',
           2: 'DG',
           3: 'BCMP',
           4: 'FHVWY',
           5: 'K',
           8: 'JZ',
           10: 'QZ'}
#   ver = int(input('Английская версия - 1 \n Русская версия - 2: '))
    if ver == 1:
        print('Вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
    elif ver == 2:
        print('Вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
    else:
        print('Ошибка ввода данных!')

print('Выберете версию игры \n Английская версия - 1 \n Русская версия - 2:')
ver = int(input())
word = input('Введите слово: ').upper()
print(scrabble(ver, word))