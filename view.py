def check_decorator(func):
    def wrapper(*args, **kwargs):
        print('########')
        print('########')
        print('########')
        print('########')
        func(*args, **kwargs)
        print('########')
        print('########')
        print('########')
        print('########')
    return wrapper
def show_menu(pizzas):
    for pizza in pizzas:
        print(pizza)
    print("Кастомная пицца")
def show_ingredients(ingredients):
    for ingredient in ingredients:
        print(ingredient)
@check_decorator
def show_check(pizzas, summ, change):
    for pizza in pizzas:
        print(f'{pizza["name"]} {pizza["count"]} X {pizza["price"]}руб.')
    print(f"Итого: {summ}руб.")
    print(f"Сдача: {change}руб.")
