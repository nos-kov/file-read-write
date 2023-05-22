from pprint import pprint

cook_book = {}


with open("recipes.txt", "rt") as recipe:

    for line in recipe:
       ingredients = []
       dish_name = line.strip()
       number = int(recipe.readline())
       for _ in range(number):
            emp = recipe.readline()
            ingr, qty, uim = emp.split(" | ")
            ingredient = {

                'ingredient_name': ingr.strip() ,
                'quantity': qty.strip(),
                'measure': uim.strip()

            }
            ingredients.append(ingredient)
       recipe.readline()
       cook_book[dish_name] = ingredients

#pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):

    output = {}

    for dish in dishes:
        for k, v in cook_book.items():
            if k == dish:
                for ingr_info in v:

                    order = {'measure': ingr_info['measure'], 'quantity': (int(person_count) * int(ingr_info['quantity']))}
                    output[ingr_info['ingredient_name']] = order
    return output


#return [(person_count* ingredient_) for ingredient_ in v if is_prime(i)]

pprint(get_shop_list_by_dishes(['Grilled Potato', 'Omelette'], 2))