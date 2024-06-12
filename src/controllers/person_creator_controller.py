from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInteface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInteface) -> None:
        self.people_repository = people_repository