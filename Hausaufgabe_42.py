""" 1. Создание базы
Напишите программу, которая:
создаёт базу данных notes_app_<your_group>_<your_full_name>
выбирает эту базу через USE notes_app
выводит сообщение о результате """

import pymysql


config = {'host': 'ich-edit.edu.itcareerhub.de',
          'user': 'ich1',
          'password': 'ich1_password_ilovedbs',
}

connection = pymysql.connect(**config)

with connection.cursor() as cursor:
    db_name = "notes_app_101025_Ruslan_Akhmetov"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
    print(f"Database {db_name} created or already exists.")
    cursor.execute(f"USE `{db_name}`")
    print()
    for row in cursor:
        print(row)


connection.close()


""" 2. Добавление заметок

Продолжите предыдущую программу:
создайте таблицу notes с полями: id, title, content
вставьте одну заметку в таблицу
выполните commit() после вставки """

import pymysql
from pymysql.cursors import DictCursor

config = {'host': 'ich-edit.edu.itcareerhub.de',
          'user': 'ich1',
          'password': 'ich1_password_ilovedbs',
          'cursorclass': DictCursor
}

connection = pymysql.connect(**config)

with connection.cursor() as cursor:
    db_name = "notes_app_101025_Ruslan_Akhmetov"

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
    print(f"Database {db_name} created or already exists.")

    cursor.execute(f"USE `{db_name}`")

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        content VARCHAR(100)
        )
    """)
    print("Table 'notes' created or already exists.")

    title = "Shopping"
    content_list = ['Milk', 'Bread', 'Eggs', 'Apples', 'Coffee']
    content = ', '.join(content_list)
    cursor.execute(""" INSERT INTO notes (title, content) VALUES (%s, %s)""", 
    (title, content))
    print(f"Note added: {title} {content_list}")

    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()

    for order, row in enumerate(rows, 1):
        print(f"{order}: {row['title']} - {row['content']}")
    
    # with DictCursor
    # for row in rows:
    #     print(f"{row['id']} {row['title']} - {row['content']}")


connection.commit()
connection.close()