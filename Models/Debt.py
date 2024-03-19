class Debt:
    def __init__(self,
                 id: int,
                 idAccount: int,
                 friend: str,
                 product: str,
                 money: float,
                 isPaid: float):
        self.id = id
        self.idAccount = idAccount
        self.friend = friend
        self.product = product
        self.money = money
        self.isPaid = isPaid

    def createDebt(self):
        return {
            "id": self.id,
            "idAccount": self.idAccount,
            "friend": self.friend,
            "product": self.product,
            "money": self.money,
            "isPaid": self.isPaid
        }
