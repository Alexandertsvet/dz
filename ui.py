

def interfase():
    print('Добрый день! /n 1 запись данных /n 2 дывод двнных')
    command = int(input('Введите число'))

    while command!=1 and command!=2:
        print('Неправильный ввод!Введите значение 1 или 2.')
        command = int(input('Введите число'))


interfase()
