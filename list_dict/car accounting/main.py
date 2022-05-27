from pathlib import Path

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

def save_file(cars:dict):
    with open('contact.txt', 'w', encoding='utf-8') as file:
        for k,v in cars.items():
            file.write(f'{k}:{v}\n')
        print('Машины записаны')

def read_file():
    f = Path('contact.txt')
    cars = {}
    if f.exists():
        with open('contact.txt', 'r', encoding='utf-8') as file:
            for i in file.readlines():
                name,car = i[:-1].split(':')
                cars.update({name: car})
    else:
        file = open('contact.txt', 'w', encoding='utf-8')
        file.close()
    return cars

def main():
    cars = read_file()
    job = {'1': add, '2': delete, '3': print_inf, '4': change}
    while True:
        jobs = input('1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Изменить машину'
                     '\n5 - Запись в файл\n6 - Выход\nВведите команду ')
        if jobs == '6':
            break
        elif jobs == '5':
            save_file(cars)
        else:
            cars = job[jobs](cars)



if __name__ == '__main__':
    main()
