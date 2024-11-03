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
