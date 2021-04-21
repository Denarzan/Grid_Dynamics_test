import random
import string
"""
Fill the chosen file with raws of random numbers.
"""
num_rows = 10000
min_amount = 1
max_amount = 100
file = 'new_test.txt'


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


with open(file, 'w') as f:
    for _ in range(num_rows):
        f.write(generate_random_string(random.randint(min_amount, max_amount)))
        f.write('\n')
