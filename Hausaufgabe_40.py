""" 1. Электронное письмо """
from datetime import datetime

class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender            # адрес отправителя
        self.recipient = recipient      # адрес получателя
        self.subject = subject          # тема письма
        self.body = body                # текст письма
        self.date = date                # дата отправки

    
    def __lt__(self, other):
        return self.date < other.date

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -"
    
    def __len__(self):
        return len(self.body)
    
    def __bool__(self):
        return bool(self.body.strip())
        # return any(not ch.isspace() for ch in self.body)
    


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print(e2)
print("Length:", len(e1))
print("Length:", len(e2))
print("Has text:", bool(e1))
print("Has text:", bool(e2))
print("Is newer:", e2 > e1)


""" 2. Класс для работы с деньгами """

class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, another_class):
        if not isinstance(another_class, Money):
            return NotImplemented
        return Money(self.amount + another_class.amount)
    
    def __sub__(self, another_class):
        if not isinstance(another_class, Money):
            return NotImplemented
        result = self.amount - another_class.amount
        if result < 0:
            result = 0
        return Money(result)
    
    def __str__(self):
        return f"${self.amount}"

money1 = Money(100)
money2 = Money(50)

print(money1)
print(money2)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)