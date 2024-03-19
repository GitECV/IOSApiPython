from Services.DBConnection import DBConnection
from Models.User import User

# Connection
dbConnection = DBConnection.dataBaseCursor()

class UserDAO:
    # Public methods
    @staticmethod
    def userLogin(email, password):
        results = dbConnection.execute('SELECT * FROM Users WHERE sMail = ? AND sPassword = ?', (email, password)).fetchall()
        dbConnection.close()
        persona1 = []
        for fila in results:
            newUser = User(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            persona1.append(newUser.createUser())
        return persona1

    @staticmethod
    def getAllUsers():
        results = dbConnection.execute('SELECT * FROM Users').fetchall()
        dbConnection.close()
        persona1 = []
        for fila in results:
            newUser = User(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            persona1.append(newUser.createUser())
        return persona1
