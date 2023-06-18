#Создайте функцию генератор чисел Фибоначчи


def fibonachi(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fibonachi(8)))