""" 1. Счётчик экземпляров """


class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return f"Total users: {cls.total_users}"


print(User.get_total())
person = User('Bob', 'fsdf2312')
print(User.get_total())
another_person = User('Alice', '54sf435F')
print(User.get_total())

"""2. Проверка данных пользователя"""


class User:
    total_users = 0

    def __init__(self, username, password):
        self.validate_data(username, password)
        self.username = username
        self.password = password
        User.total_users += 1

    @staticmethod
    def validate_data(username, password):
        if len(password) < 5:
            raise ValueError(f"Invalid password: '{password}'.\n" "Password must be at least 5 characters long.")
        elif not username:
            raise ValueError(f"Incorrect username: '{username}'.\n" "Username must not be empty ")

    @classmethod
    def get_total(cls):
        return f"Total users: {cls.total_users}"

    def __str__(self):
        return f"User: {self.username}, has password: {self.password}"


correct_person = User('Thomas', 'fsdfsdfsdfs')
# person_without_name = User('', 'dfdfsdfsd')
# person_with_short_pass = User('Alice', 'fd13')
print(correct_person)
