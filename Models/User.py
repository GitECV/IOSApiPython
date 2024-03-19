import datetime


class User:
    def __init__(self,
                 id: int,
                 name: str,
                 mail: str,
                 registerDate: datetime.datetime,
                 deactivationDate: datetime.datetime,
                 password: str,
                 isFirstEntry: bool):
        self.id = id
        self.name = name
        self.mail = mail
        self.registerDate = registerDate
        self.deactivationDate = deactivationDate
        self.password = password
        self.isFirstEntry = isFirstEntry

    def createUser(self):
        return {
            "id": self.id,
            "name": self.name,
            "mail": self.mail,
            "registerDate": self.registerDate,
            "deactivationDate": self.deactivationDate,
            "password": self.password,
            "isFirstEntry": self.isFirstEntry
        }
