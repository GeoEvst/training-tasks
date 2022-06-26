from random import *
import os
import time


def cls():
    os.system('cls')




def is_valid(n_int, rang):
    if 1 <= n_int <= rang:
        return True
    else:
        return False




def compare_with_number(n_int, random_num):
    cls()
    if n_int > random_num:
        print('Ваше число больше загаданного, попробуйте снова!')
    if n_int < random_num:
        print('Ваше число меньше загаданного, попробуйте снова!')
    if n_int == random_num:
        print('Поздравляем!!!', '\n', 'Вы угадали!', sep='')
        return True
    print(n_int)


def start_game(rang):
    print('Вы выбрали диапазон от 1 до', rang, 'включительно.')
    time.sleep(1)
    print('Хотите узнать, как играть? Введите "как" чтобы узнать правила игры либо сразу начинайте угадывать число.')
    counter = 0
    random_num = randint(1, rang)
    # print(random_num)
    while True:
        n = input()
        if n.lower() == 'как':
            print('Вам нужно угадать число, которое находится в диапазоне значений от 1 до', rang, '\n'
                  '1) Для начала игры введите число от 1 до', rang, 'включительно.', '\n'
                  '2) Мы вам подскажем больше или меньше ваше число загаданного.', '\n'
                  '3) Повторяйте попытки пока не угадаете загаданное число!', '\n' 
                  '4) Чтобы изменить диапазон введите "изменить"', '\n'
                  '5) Чтобы завершить игру введите "выход"')
        elif n.isdigit():
            n_int = int(n)
            if is_valid(n_int, rang) is False:
                print('Вы ввели неправильное число, введите число в диапазоне от 1 до', rang, 'включительно')
            else:
                counter += 1
                if compare_with_number(n_int, random_num) is True:
                    print('Количество попыток =', counter)
                    time.sleep(2)
                    print('Хотите сыграть еще раз? Введите "да" или "нет", чтобы изменить диапазон введите "изменить".')
        elif n.lower() == 'да':
            counter = 0
            random_num = randint(1, rang)
            cls()
            print('Новое число загадано, приступайте к игре!')
            # print(random_num)
        elif n.lower() == 'нет' or n.lower() == 'выход':
            print('Спасибо за игру!')
            time.sleep(2)
            break
        elif n.lower() == 'изменить':
            select_a_range()
        else:
            print('Ошибка: Введите число от 1 до', rang, 'включительно или "как", чтобы вызвать инструкцию,', '\n'
                  'Попытка ввода других символов приводит к ошибке.', '\n'
                  'Вы можете написать "Выход" чтобы завершить игру.')


def select_a_range():
    print('Введите число "n", это будет границей диапазона для загадывания чисел (от 1 до n).')
    rang = int(input())
    start_game(rang)


print('Добро пожаловать в игру "Угадай число".')
select_a_range()
