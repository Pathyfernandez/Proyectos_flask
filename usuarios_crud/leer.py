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
    def get_by_id(cls, id):
        query = "SELECT * FROM usuario WHERE id = %(id)s;"
        result = connectToMySQL('usuarios').query_db(query, {'id': id})
        if result:
            return cls(result[0])
        return None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuario (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('usuarios').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE usuario SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('usuarios').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuario WHERE id = %(id)s;"
        connectToMySQL('usuarios').query_db(query, {'id': id})
