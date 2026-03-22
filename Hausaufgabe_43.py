""" 1. Добавление товаров

Создайте программу, которая подключается к MongoDB и:
выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
очищает коллекцию перед началом
добавляет 3 товара с полями: name, price, stock
выводит сообщение о количестве добавленных товаров """


""" 2. Увеличение цен

Продолжите предыдущую задачу. Теперь программа должна:
увеличить цену всех товаров на 20%
вывести количество обновлённых записей
затем вывести список всех товаров с новыми ценами """

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

def insert_products(user_client):

    if not client.admin.command("ping")["ok"]:
        print("Connection failed!")
        return

    print("Connection successful!")
    db = user_client["ich_edit"]
    products_coll = db["products_101025_Ruslan"]
    products = products_coll.find()

    if products:
        products_coll.delete_many({})
    
    result = products_coll.insert_many([{"name": "Apple iPhone 15", "price": 899.99, "stock": 12}, 
                            {"name": "Logitech MX Master 3S", "price": 119.99, "stock": 34},
                            {"name": "Sony WH-1000XM5", "price": 349.00, "stock": 7}])
    
    print("Products inserted:", len(result.inserted_ids)) 

    update = products_coll.update_many({"stock": {"$gt": 0}}, {"$mul": {"price": 1.2 }})
    print(f"Prices updated for {update.modified_count} products") 


    products = products_coll.find()
    print("Updated products:")
    for product in products:
        print(f"- {product['name']} - ${product['price']}")

insert_products(client)


