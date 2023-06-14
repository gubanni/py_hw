# Напишите функцию для транспонирования матрицы
def trans_matrix(a_list, b_list):
    is_transparent = True
    if len(b_list) != len(a_list):
        is_transparent = False
    if is_transparent:
        return list(zip(a_list, b_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(trans_matrix([1, 8, 7, 9], [2, 4, 9, 6]))
