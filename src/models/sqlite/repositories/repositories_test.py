import pytest
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connetion_handler

# db_connetion_handler.connect_to_db()

@pytest.mark.skip(reason="integration test")
def test_list_pets():
    repo = PetsRepository(db_connetion_handler)
    response = repo.list_pets()
    print (response)

@pytest.mark.skip(reason="integration test")
def test_delete_pets():
    name = "snake"
    repo = PetsRepository(db_connetion_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="integration test")
def test_insert_person():
    first_name = "John"
    last_name = "Mich"
    age = 34
    pet_id = 2

    repo = PeopleRepository(db_connetion_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="integration test")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connetion_handler)
    response = repo.get_person(person_id)
    print(response)
