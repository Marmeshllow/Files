from pprint import pprint


def prepare_dict(file_name: str) -> dict:
    result: dict = dict()
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            recipe_name = line.strip()
            quantity_ingredient = int(file.readline())
            ingredient_list = []
            for ingredient in range(quantity_ingredient):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient_list.append(
                    {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
                )
            result[recipe_name] = ingredient_list
            file.readline()

    return result


def get_shop_list_by_dishes(cook_dict: dict, person_count: int, dishes: list) -> dict:
    result: dict = dict()
    for dish in dishes:
        for ingredient in cook_dict.get(dish):
            ingredient_name, quantity, measure = ingredient.values()
            if ingredient_name not in result.keys():
                temp_list = {'measure': measure, 'quantity': quantity * person_count}
                result[ingredient_name] = temp_list
            else:
                result[ingredient_name]['quantity'] += quantity
    return result


cook_book = prepare_dict('recipes.txt')
dishes = ['Омлет', 'Фахитос', 'Утка по-пекински']
shop_list = get_shop_list_by_dishes(cook_book, 1, dishes)
