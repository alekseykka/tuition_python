def add(contact:list):
    name = input('Введите задачу').title()
    contact.append(name)
    return contact

def delete(contact:list):
    name = input('Введите задачу').title()
    contact.remove(name)
    return contact

def print_inf(contact:list):
    for k in contact:
        print(k)
    return contact

def change(contact:list):
    name = input('Введите задачу').title()
    contact[contact.index(name)] = input('Введите новую задачу').title()
    return contact

def main():
    to_do = []
    tasks = {'1': add, '2': delete, '3': print_inf, '4': change}
    while True:

        do = input('1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Изменить номер телефона'
                     '\n5 - Выход\nВведите команду')
        if do == '5':
            break
        to_do = tasks[do](to_do)
if __name__ == '__main__':
    main()
