import random

from data.data import Person
from faker import Faker
faker_ru = Faker('ru_RU')
Faker.seed()

def generator_person():
    yield Person(
        full_name=f'{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}',
        firstname = faker_ru.first_name(),
        lastname  = faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        age=random.randint(18,80),
        salary=random.randint(1800,3000),
        department=faker_ru.job(),
    )