import pyodbc

server = 'DESKTOP-NHNJ3H0\SQLEXPRESS'
database = 'AppIOS'
username = 'admin'
password = 'admin'

connection_str = (
    f'DRIVER={{SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

conexion = pyodbc.connect(connection_str)

class DBConnection:
    @staticmethod
    def dataBaseCursor():
        return conexion.cursor();

    @staticmethod
    def closeConnection():
        conexion.close();
