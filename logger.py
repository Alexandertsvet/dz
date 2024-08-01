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
            f.write(f'{name};{surname};{phone};{address};\n')


def print_data():
    print('Вывод данных из первого файла. \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            print(*data_first)

    print('Вывод данных из второго файла. \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            print(*data_second)

def edit_data():
    print('Для редактирования файла необходимо внести новые значения.')
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
        print('Неправильный ввод!Введите значение 1 или 2.\n')
        command = int(input('Введите число'))

    if var == 1:
        with open('data_first_variant.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            index_position = int(input(f'От 0 до {int(len(data_first)/5-1)}'))*5
            print('Вы хотите изменить эти данные:\n')
            print(''.join(data_first[index_position:(index_position+4)]))
            choise = input('Вы действительно хотите изменить данные: yes or no\n')
            result = []
            if choise.lower() == 'yes':
                for i in range(0,len(data_first),5):
                    print(i)
                    if i == index_position:
                        edit_data = [f'{name}\n',f'{surname}\n',f'{phone}\n',f'{address}\n','\n']
                        result.append(edit_data)
                    else:
                        result.append(data_first[i:(i+5)])
                print(result)
                f.truncate(0)
                f.seek(0)
                for i in result:
                    print(str(''.join(i)))
                    f.writelines(i)
                print('Редактирование завершено.')

    elif var == 2:
        with open('data_second_variant.csv', 'r+', encoding='utf-8') as f:
            data_first = f.readlines()
            print(data_first)
            index_position = int(input(f'От 0 до {int(len(data_first)-1)}:'))
            print('Вы хотите изменить эти данные:\n')
            print(''.join(data_first[index_position]))
            choise = input('Вы действительно хотите изменить данные: yes or no\n')
            result = []
            if choise.lower() == 'yes':
                for i in range(len(data_first)):
                    print(i)
                    if i == index_position:
                        edit_data = f'{name};{surname};{phone};{address};\n'
                        result.append(edit_data)
                    else:
                        result.append(data_first[i])
                f.truncate(0)
                f.seek(0)
                for i in result:
                    f.writelines(i)
                print('Редактирование завершено.')
     