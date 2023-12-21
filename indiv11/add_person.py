from datetime import datetime


def add_person(people):
    """
    Добавление нового человека в список.
    Список сортируется по знаку зодиака после добавления нового элемента.
    """
    name = input("Фамилия: ")
    surname = input("Имя: ")
    date_of_birth = datetime.strptime(
        input("Введите дату рождения (в формате ДД.ММ.ГГГГ через точку): "), '%d.%m.%Y')
    zodiac_sign = input("Знак зодиака: ")

    person = {
        'name': name,
        'surname': surname,
        'date_of_birth': date_of_birth,
        'zodiac_sign': zodiac_sign
    }

    people.append(person)
    people.sort(key=lambda item: item.get('zodiac_sign', ''))
