from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name:str, last_name:str, age:int, pet_id:int):
        pass

def test_create():
    person_infos = {
        "first_name": "John",
        "last_name": "Mich",
        "age": 50,
        "pet_id": 1
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infos)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infos
