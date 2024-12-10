from view import *
from model import *
def pizzeria():
    logs = load_file('logs.json')
    log = {'name': '', 'number': '', 'order': '', 'errors': set()}
    sizes = load_file('sizes.json')
    errors = set()
    pizzas = load_file('menu.json')
    products = load_file('products.json')
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    number = input("Введите номер телефона: ")
    users = load_file('users.json')
    user = {'name': name, 'surname': surname, 'age': age, 'number': number}
    log['name'] = name
    log['number'] = number
    for data in users:
        if data['number'] == user['number']:
            print("Пользователь уже существует")
            break
    else:
        users.append(user)
        save_to_file('users.json', users)
    pizzas_name = [pizza['name'] for pizza in pizzas]
    show_menu(pizzas_name)
    user_pizzas = []
    while True:
        pizza_name = input("Что вы хотите взять(или 'стоп'): ")
        if pizza_name == 'стоп':
            break
        elif pizza_name == 'Кастомная пицца':
            size = input("Введите размер: 30, 40, 45: ")
            if find_element(size, sizes, key='size') == "Error":
                print("Размера не существует")
                errors.add(3)
                continue
            price = find_element(size, sizes, key='size')['price']
            user_products = []
            products_name = [product['name'] for product in products]
            show_ingredients(products_name)

            while True:
                product_name = input("Что вы хотите добавить(или 'стоп'): ")
                if product_name == 'стоп':
                    break
                else:
                    try:
                        product_count = int(input(f'Сколько {product_name} вы хотите добавить: '))
                        if product_count > 20:
                            print("С ума сошёл?")
                            errors.add(1)
                            continue
                    except ValueError:
                        print("Поаккуратнее")
                        errors.add(2)
                        continue
                    if find_element(product_name, products) == "Error":
                        print("Продукта не существует")
                        errors.add(3)
                    elif find_element(product_name, products)['count'] < product_count:
                        print("Извините, но этого не хватает")
                    else:
                        product_price = find_element(product_name, products)['price']
                        user_product = {'name': product_name, 'price': product_price, 'count': product_count}
                        products[products.index(find_element(product_name, products))]['count'] -= product_count
                        save_to_file('products.json', products)
                        user_products.append(user_product)
            pizza_price = calculate_custom_price(user_products, price)
            pizza_count = 1
            user_pizza = {'name': pizza_name, 'price': pizza_price, 'count': pizza_count}
            user_pizzas.append(user_pizza)
        else:
            try:
                pizza_count = int(input(f'Сколько {pizza_name} вы хотите взять: '))
                if pizza_count > 20:
                    print("С ума сошёл?")
                    errors.add(1)
                    continue
            except ValueError:
                print("Поаккуратнее")
                errors.add(2)
                continue
            if find_element(pizza_name, pizzas) == "Error":
                print("Пиццы не существует")
                errors.add(3)
            elif find_element(pizza_name, pizzas)['count'] < pizza_count:
                print("Пицц недостаточно")
            else:
                pizza_price = find_element(pizza_name, pizzas)['price']
                user_pizza = {'name': pizza_name, 'price': pizza_price, 'count': pizza_count}
                pizzas[pizzas.index(find_element(pizza_name, pizzas))]['count'] -= pizza_count
                save_to_file('menu.json', pizzas)
                user_pizzas.append(user_pizza)
    pizzas_summ = calculate_price(user_pizzas)
    print(f"Итого к оплате: {pizzas_summ}руб.")
    try:
        user_summ = int(input("Внесите сумму: "))
        if user_summ < pizzas_summ:
            print("Ты теперь должник")
            change = "По роже"
            errors.add(1)
            show_check(user_pizzas, pizzas_summ, change)
    except ValueError:
        print("Ты теперь должник")
        change = "По роже"
        errors.add(2)
        show_check(user_pizzas, pizzas_summ, change)
    else:
        change = user_summ - pizzas_summ
        show_check(user_pizzas, pizzas_summ, change)
    log['order'] = user_pizzas
    log['errors'] = list(errors)
    logs.append(log)
    save_to_file('logs.json', logs)