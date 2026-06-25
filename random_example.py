import random
import string

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_string(max_length=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, max_length)))

def random_numbers():
    return random.randint(0, 10), random.randint(-7, 7)

def random_choice_examples():
    l = [1, 59, 126, 74, 28, 183, 74]
    d = (1, 2, 3, 4, 57, 76)
    return random.choice(l), random.choice(d)

def shuffle_list():
    lst = list(range(1, 11))
    random.shuffle(lst)
    return lst
