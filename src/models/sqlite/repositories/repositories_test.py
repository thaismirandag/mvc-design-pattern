import pytest
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connetion_handler

# db_connetion_handler.connect_to_db()

@pytest.mark.skip(reason="integration test")
def test_list_pets():
    repo = PetsRepository(db_connetion_handler)
    response = repo.list_pets()
    print (response)

def test_delete_pets():
    name = "snake"
    repo = PetsRepository(db_connetion_handler)
    repo.delete_pets(name)
