res = list()
array = [2, 2, 3, 3, 4]
for el in array:
    counter = array.count(el)
    if counter > 1:
        if el not in res:
            res.append(el)
print(res)