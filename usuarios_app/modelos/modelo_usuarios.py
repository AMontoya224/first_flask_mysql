from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__( self, id, first_name, last_name, email, fecha ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.fecha = fecha
    
    @classmethod
    def agregaUsuario( cls, nuevoUsuario ):
        query = "INSERT INTO users(first_name, last_name, email, created_at, update_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(fecha)s, %(fecha)s);"
        resultado = connectToMySQL( "mydb" ).query_db( query, nuevoUsuario )
        return resultado
    
    @classmethod
    def obtenerListaUsuarios( self ):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL( "mydb" ).query_db( query )
        users = []
        for usuario in resultado:
            users.append( Usuario( usuario["id"], usuario["first_name"], usuario["last_name"], usuario["email"], usuario["created_at"]))
        return users