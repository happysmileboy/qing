import string
import random


def generate_random_string(length=60):
    choice_set = string.ascii_letters + string.digits
    num =1
    random_string =''
    while num <=20:
        num += 1
        random_string.join(random.choice(choice_set))

    return random_string