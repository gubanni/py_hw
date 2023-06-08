from random import randint

def guess_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 100
    COUNT_TRY = 9
    RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
    is_win = True
    for _ in range(COUNT_TRY + 1):
        number = int(input('Введи число от 0 до 1000: '))
        if number > RAND_NUMBER:
            print('Ваше число БОЛЬШЕ загаданного')
            is_win = False
        elif number < RAND_NUMBER:
            print('Ваше число МЕНЬШЕ загаданного')
            is_win = False
        else:
            
            print('Вы выиграли!')
            is_win = True
    if not is_win:
        print('К сожалению вы проиграли')

guess_number()