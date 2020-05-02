
def create_cook_book(initial_file):
    cook_book = {}
    while True:
        dish_name = initial_file.readline().strip()
        if not dish_name:
            break
        cook_book[dish_name] = []

        q_ingredients = int(initial_file.readline().strip())

        i = 0
        while i < q_ingredients:
            i += 1
            key_for_ingredient = ['ingredient_name', 'quantity', 'measure']
            ingredient = initial_file.readline().strip().split(' | ')
            ingredient[1] = int(ingredient[1])
            zip_of_ingredient = zip(key_for_ingredient, ingredient)
            ingredient_dict = dict(zip_of_ingredient)
            cook_book[dish_name].append(ingredient_dict)

        initial_file.readline()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        import copy
        ingredient_value = copy.deepcopy(cook_book[dish])
        i = 0
        for ingredient in cook_book[dish]:
            key_for_shop_list = ingredient['ingredient_name']
            if key_for_shop_list not in ingredient_value[i].keys():
                del(ingredient_value[i]['ingredient_name'])
            if key_for_shop_list not in shop_list_by_dishes.keys():
                shop_list_by_dishes[key_for_shop_list] = ingredient_value[i]
            else:
                new_quantity = shop_list_by_dishes[key_for_shop_list]['quantity'] + ingredient['quantity']
                shop_list_by_dishes[key_for_shop_list]['quantity'] = new_quantity
            i += 1
    for ingredient in shop_list_by_dishes.values():
        ingredient['quantity'] *= person_count

    print(shop_list_by_dishes)

with open('recipes.txt', encoding='utf8') as f:
    cook_book = create_cook_book(f)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
