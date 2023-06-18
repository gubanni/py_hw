# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


names = ['Евгений', 'Петр', 'Тимур', 'Алексей']
salarys = [35000, 25000, 19000, 40000]
bonuses = ['10.00%', '15.25%', '16.50%', '10.05%']


def premia(names: list[str], salarys: list[int], bonuses: list[str]) -> dict[str: float]:
    return {name: round(salary / 100 * bonus, 2) for name, salary, bonus in zip(names, salarys, (float(i[:-1]) for i in bonuses))}.items()


print(premia(names, salarys, bonuses))