try:
    number = int(input('Введите число от 1 до 100_000: '))
    if 0 < number <= 100_000:
        print('Ok')
    else:
        print('Число должно быть от 1 до 100_000')
except ValueError:
    
    print('Введите целое число от 1 до 100_000')

type = 'простое'
if not number % 2:
    type = 'составное'
else:
    for dev in range(3, number // 2 + 1, 2):
        if not number % dev:
            type = 'составное'

print(type)