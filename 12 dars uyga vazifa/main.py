print('hello world')


print("Salom dunyo")

import random
import string


def id_generator(length=4):
    random_id = string.digits
    user_id = ""
    for i in range(length):
        user_id += random.choice(random_id)
    return user_id


print(id_generator())

name = input("Ismingizni kiriting: ")


def add_num(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    else:
        return 'Musbat son kiriting!'


print(add_num(10, 4))
