import datetime


class Account:
    def __init__(self,
                 id: int,
                 idUser: int,
                 name: str,
                 lastModified: datetime.datetime,
                 description: float):
        self.id = id
        self.idUser = idUser
        self.name = name
        self.lastModified = lastModified
        self.description = description

    def createAccount(self):
        return {
            "id": self.id,
            "idUser": self.idAccount,
            "name": self.friend,
            "lastModified": self.product,
            "description": self.money
        }
