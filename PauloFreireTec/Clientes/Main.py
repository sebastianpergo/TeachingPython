# Imports
import os

# Declaro lista vacia
usuarios = []


def MenuPrincipal():
    os.system('clear')
    print("Menu Principal")
    print("1. Registrar Usuarios")
    print("2. Listar Usuarios")
    print("3. Actualizar Usuarios")
    print("4. Eliminar Usuarios")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        RegistrarUsuarios()
    elif opcion == "2":
        ListarUsuarios()
    elif opcion == "3":
        BuscarUsuarios()
    elif opcion == "4":
        EliminarUsuarios()
    elif opcion == "5":
        exit()


def RegistrarUsuarios():
    os.system('clear')
    print("Registrar Usuarios")
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    email = input("Ingrese el email del usuario: ")
    usuario = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email
    }
    usuarios.append(usuario)
    print("Usuario registrado con exito")
    input("Presione una tecla para continuar...")
    MenuPrincipal()


def ListarUsuarios():
    os.system('clear')
    print("Listar Usuarios")
    print("Nombre\t     Apellido\t      Email")
    for usuario in usuarios:
        print(usuario['nombre'] + "\t" +
              usuario['apellido'] + "\t" + usuario['email'])
    input("Presione una tecla para continuar...")
    MenuPrincipal()


def BuscarUsuarios():
    os.system('clear')
    print("Buscar Usuarios")
    email = input("Ingrese el email del usuario: ")
    for usuario in usuarios:
        if usuario['email'] == email:
            print("Nombre\t     Apellido\t      Email")
            print(usuario['nombre'] + "\t" +
                  usuario['apellido'] + "\t" + usuario['email'])
    input("Presione una tecla para continuar...")
    MenuPrincipal()


def EliminarUsuarios():
    os.system('clear')
    print("Eliminar Usuarios")
    email = input("Ingrese el email del usuario: ")
    for usuario in usuarios:
        if usuario['email'] == email:
            usuarios.remove(usuario)
    print("Usuario eliminado con exito")
    input("Presione una tecla para continuar...")
    MenuPrincipal()


if __name__ == '__main__':
    MenuPrincipal()
