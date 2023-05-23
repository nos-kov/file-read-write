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
    order = {}
    counter = 0 
    for dish in dishes:
        for k, v in cook_book.items():
            if k == dish:
                for ingr_info in v:

                    if ingr_info['ingredient_name'] in output:
                        counter += 1
                        
                    order = {'measure': ingr_info['measure'], 'quantity': (int(person_count) * int(ingr_info['quantity']))}
                    if counter > 0 and ingr_info['ingredient_name'] in output:#stop zdezi - proverka chto ingredient uzhe v output a ne v order
                        order.update({'quantity': output[ingr_info['ingredient_name']].get('quantity', 0) + (int(person_count) * int(ingr_info['quantity']))})

                    output[ingr_info['ingredient_name']] = order
                    
    return output


#return [(person_count* ingredient_) for ingredient_ in v if ]

pprint(get_shop_list_by_dishes(['Omelette', 'Fajitos', 'Omelette'], 2))