from pprint import pprint


def prepare_dict(file_name: str) -> dict:
    result: dict = dict()
    with open('recipes.txt', encoding='utf-8') as file:
        for line in file:
            recipe_name = line.strip()
            quantity_ingredient = int(file.readline())
            ingredient_list = []
            for ingredient in range(quantity_ingredient):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient_list.append(
                    {'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()}
                )
            result[recipe_name] = ingredient_list
            file.readline()

    return result


cook_book = prepare_dict('recipes.txt')
pprint(cook_book, indent=4)
