# 1. Деление без ошибок

def division_to_null():
    a = input("Enter please first number: ")
    b = input("Enter please second numbers: ")
    try:
        return int(a) / int(b)
    except (ZeroDivisionError, ValueError, TypeError):
        return f"ERROR! Incorrect number"


print(division_to_null())


##############################################################################

def safe_divide():
    try:
        num1 = float(input("Enter please first number: "))
        num2 = float(input("Enter please second numbers: "))
        return num1 / num2
    except ValueError:
        print(f"ERROR! Incorrect number")
    except ZeroDivisionError:
        print(f"ERROR! Incorrect number")


result = safe_divide()
if result is not None:
    print(f"Result: {result}")

# 2. Логирование ошибок
# import logging, os
#
# logging.basicConfig(filename='errors.log', level=logging.ERROR,
#                     format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
#
#
# def division_to_null():
#     a = input("Enter please first number: ")
#     b = input("Enter please second numbers: ")
#     try:
#         return int(a) / int(b)
#     except (ZeroDivisionError, ValueError, TypeError):
#         logging.error("ERROR! Incorrect number")
#
#
# print(division_to_null())


##############################################################################

import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')


def safe_divide():
    try:
        num1 = float(input("Enter please first number: "))
        num2 = float(input("Enter please second numbers: "))
        return num1 / num2
    except ValueError:
        print(f"ERROR! Incorrect number")
    except ZeroDivisionError:
        print(f"ERROR! Incorrect number")


result = safe_divide()
if result is not None:
    print(f"Result: {result}")
