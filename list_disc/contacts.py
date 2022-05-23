def add(contact:dict):
    name = input('Введите имя').title()
    if contact.get(name):
        print(f'{name} есть в контактах')
    contact[name] = int(input('Введите телефон'))
    return contact

def delete(contact:dict):
    name = input('Введите имя').title()
    if contact.get(name):
        contact.pop(name)
        print(f'{name} удален')
    else:
        print(f'{name} не найден')
    return contact

def print_inf(contact:dict):
    for k,v in contact.items():
        print(f'{k} - {v}')
    return contact

def change(contact:dict):
    name = input('Введите имя').title()
    if contact.get(name):
        contact[name] = int(input('Введите телефон'))
    return contact

def main():
    contact = {'Alex':123456,'Lena':2546987,'Vova':985647}
    job = {'1': add, '2': delete, '3': print_inf,'4': change}

    while True:
        jobs = input('1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Изменить номер телефона'
                     '\n5 - Выход\nВведите команду')
        if jobs == '5':
            break
        contact = job[jobs](contact)





if __name__ == '__main__':
    main()
