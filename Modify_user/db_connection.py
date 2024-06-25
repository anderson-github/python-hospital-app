import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        # Inicializa la conexión a la base de datos
        self.connection = None
        try:
            # Intenta establecer la conexión con los parámetros proporcionados
            self.connection = mysql.connector.connect(
                host='localhost',
                database='hospital_bdd',
                user='root',
                password=''
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            # Captura y muestra cualquier error durante la conexión
            print(f"Error al conectar a la base de datos: {e}")

    def get_users(self):
        # Obtiene todos los usuarios de la base de datos
        if self.connection.is_connected():
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT id_usuario, nombre, apellido FROM usuarios")
            return cursor.fetchall()  # Devuelve una lista de diccionarios
        return []  # Retorna una lista vacía si no hay conexión

    def get_user(self, user_id):
        # Obtiene los datos de un usuario específico por su ID
        if self.connection.is_connected():
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
            return cursor.fetchone()  # Devuelve un diccionario con los datos del usuario
        return None  # Retorna None si no hay conexión o no se encuentra el usuario

    def update_user(self, user_id, field, value):
        # Actualiza un campo específico de un usuario
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            # Construye la consulta SQL de actualización
            query = f"UPDATE usuarios SET {field} = %s WHERE id_usuario = %s"
            cursor.execute(query, (value, user_id))
            self.connection.commit()  # Confirma los cambios en la base de datos
            return cursor.rowcount > 0  # Retorna True si se actualizó al menos una fila
        return False  # Retorna False si no hay conexión

    def close_connection(self):
        # Cierra la conexión a la base de datos
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")