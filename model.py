import json
def find_element(element, object, key='name'):
    for elem in object:
        if elem[key] == element:
            return elem
    return "Error"
def save_to_file(filename, object):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(object, file, indent=4)
def load_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        return json.load(file)
def calculate_custom_price(ingredients, size):
    summ = 0
    for ingredient in ingredients:
        summ += ingredient['count'] * ingredient['price']
    summ += size
    return summ
def calculate_price(pizzas):
    summ = 0
    for pizza in pizzas:
        summ += pizza['count'] * pizza['price']
    return summ
