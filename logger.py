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
    f'{name};{surname};{phone};{address};\n'
    f'Выберите вариант.'
    ))

def print_data():
    pass


input_data()