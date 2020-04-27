with open('recipes.txt', encoding='utf8') as f:
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        cook_book[dish_name] = []

        q_ingredients = int(f.readline().strip())

        i = 0
        while i < q_ingredients:
            i += 1
            key_for_ingredient = ['ingredient_name', 'quantity', 'measure']
            ingredient = f.readline().strip().split(' | ')
            ingredient[1] = int(ingredient[1])
            zip_of_ingredient = zip(key_for_ingredient, ingredient)
            ingredient_dict = dict(zip_of_ingredient)
            cook_book[dish_name].append(ingredient_dict)

        f.readline()

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        ingredient_value = cook_book[dish]
        for ingredient in ingredient_value:
            key_for_shop_list = ingredient['ingredient_name']
            del(ingredient['ingredient_name'])
            if key_for_shop_list not in shop_list_by_dishes.keys():
                shop_list_by_dishes[key_for_shop_list] = ingredient
            else:
                new_quantity = shop_list_by_dishes[key_for_shop_list]['quantity'] + ingredient['quantity'] * person_count
                shop_list_by_dishes[key_for_shop_list]['quantity'] = new_quantity
                continue
            shop_list_by_dishes[key_for_shop_list]['quantity'] *= person_count

    print(shop_list_by_dishes)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)