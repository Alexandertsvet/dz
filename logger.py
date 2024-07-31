from data_cereate import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'формат записи \n\n'
    f'1 первый вариант\n'
    f'{name}\n{surname}\n{phone}\n{address}\n\n'
    f'2 второй вариант\n'
    f'{name};{surname};{phone};{address};\n\n'
    f'Выберите вариант.'
    ))
    while var!=1 and var!=2:
        print('Неправильный ввод!Введите значение 1 или 2.')
        command = int(input('Введите число'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address};\n\n')


def print_data():
    print('Вывод данных из первого файла.')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            
                


print_data()