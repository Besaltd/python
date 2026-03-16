""" 1. Список всех стран

Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой строки и иметь номер. """

import pymysql

config = {'host': 'ich-db.edu.itcareerhub.de', 'user': 'ich1', 'password': 'password', }

connection = pymysql.connect(**config)

with connection.cursor() as cursor:
    cursor.execute("USE world")
    cursor.execute("SELECT * FROM country")
    for order, name in enumerate(cursor, 1):
        print(f"{order}. {name[1]}")

""" 2. Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка. Далее выведите все города этой страны и их численность населения, также с нумерацией."""

import pymysql

config = {'host': 'ich-db.edu.itcareerhub.de', 'user': 'ich1', 'password': 'password', }

connection = pymysql.connect(**config)

with connection.cursor() as cursor:
    cursor.execute("USE world")
    cursor.execute("SELECT * FROM country")
    rows = cursor.fetchall()

    for order, name in enumerate(rows, 1):
        print(f"{order}. {name[1]}")

    countries = dict(enumerate((val[1] for val in rows), 1))

    country_name = input("Enter name or order country: ")

    try:
        num = int(country_name)
        country_name = countries[num]
    except ValueError:
        pass

    cursor.execute("""
                   SELECT city.Name, city.Population
                   FROM country
                            JOIN city
                                 ON country.Code = city.CountryCode
                   WHERE country.Name = %s """, country_name)

    for order, (city, population) in enumerate(cursor, 1):
        print(f"{order}. {city} - {population}")

connection.close()
