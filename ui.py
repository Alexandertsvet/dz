from logger import input_data, print_data, edit_data, delete_data, migrate_data

def interfase():
    print('Добрый день! \n 1 запись данных \n 2 вывод двнных \n 3 редакция данных \n 4 удаление данных \n 5 пермешение данных \n')
    command = int(input('Введите число:'))

    while command!=1 and command!=2 and command!=3 and command!=4 and command!=5:
        print('Неправильный ввод!Введите значение 1 или 2.')
        command = int(input('Введите число'))

    if command==1:
        input_data()
    if command==2:
        print_data()
    if command==3:
        edit_data()
    if command==4:
        delete_data()
    if command==5:
        migrate_data()
    

