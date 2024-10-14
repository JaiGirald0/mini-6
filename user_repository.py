"""
Este archivo contiene la lógica para:

1. Crear un usuario
2. Actualizar información de un usuario
3. Obtener todos los usuarios
4. Obtener información de un usuario específico
"""
import os
import json
from models.users import users  # Importación del modelo de usuarios

# Definir las rutas para cargar y guardar los datos de usuarios
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "user.json")


def load_users():
    """
    Carga los datos de usuarios desde el archivo JSON y los almacena en la variable global 'users'.
    """
    global users
    with open(JSON_PATH, "r") as f:
        users = json.load(f)  # Cargar usuarios desde el archivo JSON

    return users  # Retorna los usuarios cargados


def save_users(new_info):
    """
    Guarda la información actualizada de los usuarios en el archivo JSON.
    
    :param new_info: Diccionario que contiene la información actualizada de los usuarios.
    """
    with open(JSON_PATH, "w") as f:
        json.dump(new_info, f, indent=4)  # Guardar los datos en el archivo con formato


def get_users(username):
    """
    Obtiene la información de un usuario específico.

    :param username: El nombre de usuario a buscar.
    :return: Información del usuario si existe, de lo contrario None.
    """
    return users.get(username)  # Retorna la información del usuario si existe


def create_user(username, user_info):
    """
    Crea un nuevo usuario y lo añade al diccionario de usuarios.

    :param username: El nombre de usuario del nuevo usuario.
    :param user_info: Diccionario que contiene la información del nuevo usuario.
    """
    if username in users:
        raise ValueError(f"El usuario {username} ya existe.")  # Controla que no se cree un usuario duplicado

    users[username] = user_info  # Añade el nuevo usuario al diccionario de usuarios
    save_users(users)  # Guarda los cambios en el archivo JSON
