# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

BEARING_CAPACITY = 5000

things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
      	'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
          'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}

backpack = 0
backpack_dictionary = {}

for key, item in things.items():
    if backpack + item <= BEARING_CAPACITY:
        backpack_dictionary[key] = item
        backpack += item

print(f'Содержимое рюкзака: {backpack_dictionary}.\n Вес рюкзака составил: {backpack} грамм.')
