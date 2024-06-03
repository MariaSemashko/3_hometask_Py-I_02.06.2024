'''Создайте словарь со списком вещей для похода в качестве ключа и
их массой в качестве значения. Определите какие вещи влезут в рюкзак
передав его максимальную грузоподъёмность. Достаточно вернуть один
допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.'''

hike = {
    'Спальник': 2,
    'Пенка': 1,
    'Топор' : 4,
    'Саперка' : 2,
    'Теплая одежда' : 5,
    'Еда' : 10,
    'Вода' : 15,
    'Котелок' : 2,
    'Посуда' : 3,
    'Фотоаппарат' : 1,
    'Палатка' : 20,
}

capacity = int(input('введите максимальную грузоподъемность рюкзака: '))

result = []
weight = 0
for key in hike:
    weight += hike[key]
    if  weight < capacity:
        result.append(key)
    else:
        weight -= hike[key]
        break

print(f'В рюкак влезут следующие вещи: {result}, вес рюкзака {weight}')
print()

for key in hike:
    result_2 = [key]
    weight_2 = hike[key]
    for other_key in hike:
        if other_key != key:
            weight_2 += hike[other_key]
            if weight_2 < capacity:
                result_2.append(other_key)
            else:
                weight_2 -= hike[other_key]
                break
    print(f'Вариант комплектации рюкзака: {result_2}, вес рюкзака {weight_2}')