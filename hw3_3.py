skrab = {'sapogi': 1, 'udochka': 2, 'eda': 10, 'voda': 5, 'spichki': 3}
vmestimost = 10
packaging_option = {}
for key, value in skrab.items():
    if value <= vmestimost:
        vmestimost -= value
        packaging_option[key] = value
# если осталось место в рюкзаке дозаполняем его частью вещей
if vmestimost > 0:
    for key, value in skrab.items():
        if key not in packaging_option:
            packaging_option[key] = vmestimost
            vmestimost = 0
            break
print(packaging_option)
