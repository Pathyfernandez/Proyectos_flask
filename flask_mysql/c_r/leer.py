from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['fecha_creacion']
        self.updated_at = data['fecha_actualizacion']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuario;"
        results = connectToMySQL('usuarios').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuario (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('usuarios').query_db(query, data)
