import random

def main():
    while True:
        rnd = random.randrange(15)
        rnd_user = int(input("Угадай число от 0 до 15 \n"))

        if rnd == rnd_user:
            print("Вы угадали число )")
        else:
            print('Вам не повезло (')

        res = input('Хотите сыграть еще ? y/n \n')

        if res == 'y':
            continue
        elif res == 'n':
            print('Хорошего дня )')
            break

if __name__ == '__main__':
    main()