cook_book = {}
with open('file.txt', 'rt') as file:
    for i in file:
        i = i.strip()
        cook_book[i] = []
        ingridient_count = file.readline()
        for s in range(int(ingridient_count)):
            ing = file.readline()
            ing = ing.strip()
            ingridient_name, quantity, measure = ing.split(' | ')
            cook_book[i].append({'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    buy_list = {}
    for i in dishes:
        if i in cook_book:
            for j in cook_book[i]:
                if j['ingridient_name'] not in buy_list:
                    buy_list[j['ingridient_name']] = {'measure' : j['measure'], 'quantity' : int(j['quantity']) * person_count}
                else:
                    buy_list[j['ingridient_name']].get('quantity', 0) + int(j['quantity']) * person_count
        else:
            return f'''Ingridient {i} doesn't in cook book. Please, try again.'''
    return buy_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2))