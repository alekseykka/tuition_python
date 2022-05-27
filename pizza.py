def choice_of_ingredients():
    ingredients = ('сыр Моцарелла','шампиньоны','бекон','лук','орегано')
    selected_ingredients = list()
    for ingredient in ingredients:
        while True:
            option = input(f'Желаете добавить {ingredient}? y/n\n').lower()
            if option == 'y':
                selected_ingredients.append(ingredient)
                break
            elif option == 'n':
                break
            else:
                print('Неверно узазана команда')
    print(selected_ingredients)
    selection_check()

def selection_check():
    check = input('Верный заказ? y/n \n')
    if check == 'n':
        choice_of_ingredients()
    elif check == 'y':
        print('Ожидайте заказ')
        exit()

def main():
    while True:
        order = input('Желаете сделать заказ ? y/n\n').lower()
        if order == 'y':
            choice_of_ingredients()
        elif order == 'n':
            print('Хорошего дня')
            break

if __name__ == '__main__':
    main()
