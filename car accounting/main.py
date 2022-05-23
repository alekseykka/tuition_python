def add(contact:dict):
    name = input('Введите имя').title()
    if contact.get(name):
        print(f'{name} есть в контактах')
    contact[name] = input('Введите машину')
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
        contact[name] = input('Введите машину')
    return contact

def main():
    with open('contact.txt','r+',encoding='utf-8') as file:
        contact = file.read()

    contact = {'Alex': 'BMW', 'Lena': 'Audi', 'Vova': 'Volvo'}
    job = {'1': add, '2': delete, '3': print_inf, '4': change}

    while True:
        jobs = input('1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Изменить машину'
                     '\n5 - Выход\nВведите команду')
        if jobs == '5':
            break
        contact = job[jobs](contact)

    with open('contact.txt','r+',encoding='utf-8') as file:
        file.write(str(contact))

if __name__ == '__main__':
    main()
