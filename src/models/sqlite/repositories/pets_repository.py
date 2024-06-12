from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def list_pets(self) -> list:
        with self.db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name:str) -> None:
        with self.db_connection as database:
            try:
                (
                    database.session
                    .query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
