# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'year': fake.random_number(digits=4, fix_len=True),
        'year_time_unit': 'Ano',
        'kilometers': fake.random_number(digits=6, fix_len=True),
        'kilometers_unit': 'Quilometros',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/car,vehicle' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
