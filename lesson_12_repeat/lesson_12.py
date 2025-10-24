height_data = {
    'person1': {'gender': 'Male', 'height': None},
    'person2': {'gender': 'Female', 'height': None},
    'person3': {'gender': 'Male', 'height': None}

}


def average_height(height_data):
    try:
        heights = [float(person['height']) for person in height_data.values() if 'height' in person]
        if not heights:
            raise ValueError("No height data provided.")
        return round(sum(heights) / len(heights), 2)
    except (TypeError, ValueError) as e:
        print(f"Error calculating average: {e}")
        return None


# print(average_height(height_data))

"""Список містить словники - дані про ціну і тираж кожного з журналів. Скласти програму, яка визначає середню вартість журналів, тираж яких більше 10 000 примірників.
Помилка"""
data = [
    {"name": "Space", "volume": 20000, "price": 5},
    {"name": "SeaSide", "volume": 10000, "price": 5},
    {"name": "Fortune", "volume": 10000, "price": 0},
    {"name": "Vouge", "volume": 25000, "price": '10.00'},
]


# res = [x['price'] for x in data if x['volume'] > 10000]

def average_price(data):
    try:
        result = []
        for x in filter(lambda x: x.get("volume", 0) >= 10000, data):

            price = x.get("price", 0)
            try:
                price = float(price) if price is not None else 0
            except (TypeError, ValueError, KeyError) as e:
                raise ValueError(f"Error calculating average price: {e}.")
            result.append(price)
        if not result:
            raise ValueError("No data provided.")
        print(result)
        return round(sum(result) / len(result), 2)

    except (TypeError, ValueError) as e:
        raise ValueError(f"Error calculating average: {e}")

# print(average_price(data))

"""Задано дані (список списків) про багаж (кількість речей і загальна вага багажу) 
пасажирів. Скласти функцію, яка повертає тапл де міститься: 
а) кількість пасажирів, які мають більше двох речей; 
б) чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг;
 в) число пасажирів, кількість речей яких перевершує середнє число речей всіх пасажирів."""
data = [
    {'number_of_items': '1', 'total_weight': 25},
    # {'number_of_items': 3.9, 'total_weight': 24}
]

def luggage_check(data):

    if not isinstance(data, list):
        raise TypeError("Data must be a list of dictionaries.")

    items_count = [x.get("number_of_items") for x in data if isinstance(x.get("number_of_items"), int)]
    if not items_count:
        raise ValueError("No data provided.")
    count_over_2 = sum(list(map(lambda x: x > 2, items_count)))
    is_has_weight_under_25 = any(map(lambda x: x.get("number_of_items") == 1 and x.get("total_weight") < 25, data))
    avg_items = sum(items_count)/len(items_count)
    count_over_avg = len([x for x in items_count if x > avg_items])

    return (count_over_2, is_has_weight_under_25, count_over_avg)
# print(luggage_check(data))