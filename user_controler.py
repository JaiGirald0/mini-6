"""
Este archivo contiene la lógica para interactuar con el usuario
y realizar operaciones sobre los datos de usuarios a través del servicio 'user_service'.
"""
import user_service

def get_user():
    """
    Solicita al usuario un nombre de usuario, lo busca en el sistema 
    utilizando el servicio 'user_service', y muestra la información obtenida o un mensaje si no se encuentra.
    """
    username = input("Ingrese el nombre de usuario: ").strip()
    
    if not username:  # Validación para evitar entradas vacías
        print("El nombre de usuario no puede estar vacío.")
        return
    
    response = user_service.get_user(username)
    if response:
        print(response)
    else:
        print(f"El usuario {username} no está registrado.")


def menu():
    """
    Muestra el menú de opciones al usuario.
    """
    message = """\
    Seleccione una opción:

    1. Obtener información de un usuario
    2. Obtener lista de usuarios
    3. Crear usuario
    4. Actualizar información de un usuario
    5. Salir
    """
    print(message)


def main():
    """
    Función principal que carga los usuarios, muestra el menú y maneja la lógica de selección de opciones.
    """
    flag = True
    user_service.user_repository.load_users()  # Cargar usuarios al iniciar el programa
    
    while flag:
        menu()
        option = input("Opción: ").strip()
        
        # Validar y manejar las opciones del menú
        if option == "1":
            get_user()
        elif option == "2":
            print("Funcionalidad de obtener lista de usuarios no implementada aún.")
        elif option == "3":
            print("Funcionalidad de crear usuario no implementada aún.")
        elif option == "4":
            print("Funcionalidad de actualizar usuario no implementada aún.")
        elif option == "5":
            print("Saliendo del programa...")
            flag = False  # Salir del bucle
        else:
            print("Opción no válida. Inténtelo de nuevo.")


# Ejecutar el programa solo si este archivo es el principal
if __name__ == "__main__":
    main()
