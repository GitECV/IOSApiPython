from flask import Flask, jsonify, request

from Services.UsersDAO import UserDAO

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta básica
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(UserDAO.userLogin(data['email'], data['password']))

# Comprobamos si el archivo se está ejecutando directamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
