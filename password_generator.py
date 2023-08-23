# python code for creating a random strong password generator
# Make the below code according to Pep8 standards

import random
import string


def password_generator():
    password = ""
    for i in range(12):
        password += random.choice(
            string.ascii_letters + string.digits + string.punctuation
        )
    return password


print(password_generator())
