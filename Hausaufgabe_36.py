# 1. Класс Person

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

# 2. Класс Student

class Student(Person):
    def __init__(self, name, course_number):
        super().__init__(name)
        self.course_number = course_number

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course_number}.")

# 3. Класс Teacher и список людей

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}. My subject is {self.subject}.")

people = [Student('Alice', 2), Teacher('Bob', 'Mathematics')]

for person in people:
    person.introduce()