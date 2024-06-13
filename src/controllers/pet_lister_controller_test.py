from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Mica", type="cat", id=2),
            PetsTable(name="Enri", type="dog", id=5),
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
                    "type": "Pets",
                    "count": 2,
                    "atributes": [
                        {"name":"Mica", "id": 2},
                        {"name":"Enri", "id": 5}
                                  ]
                }
    }

    assert response == expected_response
