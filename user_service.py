"""
Este archivo contiene la lógica para:

1. Crear un usuario
2. Actualizar información de un usuario
3. Obtener todos los usuarios
4. Obtener información de un usuario específico
"""
import user_repository

def get_user(username):
    """
    Obtiene la información de un usuario específico.
    
    :param username: El nombre de usuario a buscar.
    :return: Información del usuario si existe, de lo contrario None.
    """
    return user_repository.get_users(username)


def create_user(username, **kwargs):
    """
    Crea un nuevo usuario con la información proporcionada.

    :param username: El nombre de usuario del nuevo usuario.
    :param kwargs: La información del usuario, que debe incluir 'name', 'ocupation' y 'password'.
    :raises Exception: Si el usuario ya existe o si la estructura de la información es incorrecta.
    """
    # Verifica si el usuario ya existe
    if user_repository.get_users(username):
        raise Exception(f"El usuario {username} ya existe.")
    
    # Validar que se hayan proporcionado los 3 campos esperados ('name', 'ocupation', 'password')
    required_keys = ["name", "ocupation", "password"]
    
    if not all([key in kwargs for key in required_keys]):
        raise Exception(f"La información del usuario no tiene la estructura esperada. Se necesitan las llaves: {', '.join(required_keys)}")
    
    # Aquí puedes agregar cualquier validación adicional que necesites antes de crear el usuario
    
    # Mostrar la información del usuario antes de guardarlo (debugging)
    print("Información del nuevo usuario:", kwargs)
    
    # Guardar el nuevo usuario (esto asumiría que tienes una función en el user_repository para guardar usuarios)
    user_repository.create_user(username, kwargs)


# Ejemplo de creación de usuario
create_user(
    "pepito",
    name="Pepito Pérez",
    ocupation="Programador",
    password="seguro123",
    gender="male"  # Aunque 'gender' no es un campo obligatorio, puede incluirse
)
