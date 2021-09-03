import os
from operator import itemgetter
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


def get_shop_list_by_dishes(cook_dict: dict, person_count: int, dish_dict: list) -> dict:
    result: dict = dict()
    for dish in dish_dict:
        for ingredient in cook_dict.get(dish):
            ingredient_name, quantity, measure = ingredient.values()
            if ingredient_name not in result.keys():
                temp_list = {'measure': measure, 'quantity': quantity * person_count}
                result[ingredient_name] = temp_list
            else:
                result[ingredient_name]['quantity'] += quantity
    return result


def compare_file(path='Text_files'):
    result = []
    files = os.listdir(path)
    for text_file in files:
        with open(path+'/'+text_file, 'r', encoding='utf-8') as file:
            count_line = 0
            text = ''
            for line in file:
                count_line += 1
                text += line
            result.append([text_file, count_line, text])
    sorter_list = sorted(result, key=itemgetter(1), reverse=True)
    with open('result.txt', 'w', encoding='utf-8') as file:
        for elm in sorter_list:
            result_str = f'{elm[0]}\n{str(elm[1])}\n{elm[2]}\n'
            file.write(result_str)


cook_book = prepare_dict('recipes.txt')
dishes = ['Омлет', 'Фахитос', 'Утка по-пекински']
shop_list = get_shop_list_by_dishes(cook_book, 1, dishes)
pprint(shop_list)
compare_file()
